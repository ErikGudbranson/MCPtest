from mcp.server.fastmcp import FastMCP

# Create the server
mcp = FastMCP("Pontus Demo MCP")

# Simple tool: add two integers
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Adds two numbers and returns the result.
    """
    return a + b

# Simple resource: greeting by name
@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """
    Returns a friendly greeting.
    """
    return f"Hej {name}, greetings from your MCP server!"

if __name__ == "__main__":
    mcp.run()
