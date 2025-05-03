import os
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()
console = Console()

mcp = FastMCP("My Tools", port=7777)


@mcp.tool()
def get_weather_country(country: str):
    """Get Weather Country"""
    access_key = os.environ.get("ACCESS_KEY")
    url = f"https://api.weatherstack.com/current?access_key={access_key}&query={country}"
    response = requests.get(url)
    data = response.json()
    return data.get("current", [])


if __name__ == "__main__":
    console.print("Running...")
    mcp.run(transport='sse')
