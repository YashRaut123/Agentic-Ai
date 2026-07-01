from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()

async def get_weather(city: str) -> str:
    """Get the weather for a given city."""
    return "Its always raining in Seattle"



if __name__ == "__main__":
    mcp.run(transport="streamable-http")