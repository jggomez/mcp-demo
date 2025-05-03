import asyncio
import os
from google import genai
from google.genai import types
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from rich.console import Console
from dotenv import load_dotenv

load_dotenv()
console = Console()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Create server parameters for SSE connection
server_params = StdioServerParameters(
    command="mcp-proxy",
    args=["http://0.0.0.0:8000/mcp"],  # MCP Server
    env=None,  # Optional environment variables
)

current_dir = os.path.dirname(os.path.abspath(__file__))
server_path = os.path.join(current_dir, "mcp_server_demo.py")

# Create server parameters for stdio connection
# server_params = StdioServerParameters(
#    command="python",
#    args=[server_path],  # MCP Server
#    env=None,  # Optional environment variables
# )


async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            contents = [
                types.Content(
                    role="user", parts=[types.Part(text="What is the weather in Mexico?")]
                )
            ]

            # Initialize the connection between client and server
            await session.initialize()

            # Get tools from MCP session and convert to Gemini Tool objects
            mcp_tools = await session.list_tools()
            console.print(mcp_tools.tools)
            tools = [
                types.Tool(
                    function_declarations=[
                        {
                            "name": tool.name,
                            "description": tool.description,
                            "parameters": {
                                k: v
                                for k, v in tool.inputSchema.items()
                                if k not in ["additionalProperties", "$schema"]
                            },
                        }
                    ]
                )
                for tool in mcp_tools.tools
            ]

            console.print(tools)

            config = types.GenerateContentConfig(
                temperature=0.5,
                tools=tools,
            )

            # Send request to the model with MCP function declarations
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=contents,
                config=config,
            )

            # Check for a function call
            if response.candidates[0].content.parts[0].function_call:
                function_call = response.candidates[0].content.parts[0].function_call
                print(function_call)
                # Call the MCP server with the predicted tool
                result_mcp = await session.call_tool(
                    function_call.name, arguments=function_call.args
                )
                print("print............")
                result = result_mcp.content[0].text
                console.print(result)

                # Create a function response part
                function_response_part = types.Part.from_function_response(
                    name=function_call.name,
                    response={"result": result},
                )

                # Append function call and result of the function execution to contents
                contents.append(types.Content(role="model", parts=[
                                types.Part(function_call=function_call)]))
                contents.append(types.Content(
                    role="user", parts=[function_response_part]))

                final_response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    config=config,
                    contents=contents,
                )

                console.print(final_response.text)
            else:
                console.print("No function call found in the response.")
                console.print(response.text)


asyncio.run(run())
