import os
import requests
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
from dotenv import load_dotenv


load_dotenv()
app = FastAPI()


@app.get("/weather/{country}", operation_id="get_weather_country")  # Tool Name
async def get_weather_country(country: str):
    access_key = os.environ.get("ACCESS_KEY")
    url = f"https://api.weatherstack.com/current?access_key={access_key}&query={country}"
    response = requests.get(url)
    data = response.json()
    return data.get("current", [])


# Add the MCP server to your FastAPI app
mcp = FastApiMCP(
    app,
    name="MCPFastAPI",
    include_operations=["get_weather_country"],
    description="MCP server for my weather API",
    describe_all_responses=True,
    describe_full_response_schema=True,
)

# Mount the MCP server to your FastAPI app
mcp.mount()

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
