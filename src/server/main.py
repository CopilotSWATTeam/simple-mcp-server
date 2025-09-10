from fastmcp import FastMCP
from fastmcp.utilities.logging import get_logger
import io
import os
from dotenv import load_dotenv

load_dotenv()

PORT = os.environ.get("PORT")
print(PORT)

cwd = os.getcwd()
logger = get_logger("my-simple-mcp-server")

mcp = FastMCP("My MCP Server")

@mcp.tool 
def add(a: int, b: int) -> int:
    """ This is a simple tool that will add two numbers together."""
    return a + b

@mcp.tool
def subtract(a: int, b: int) -> int:
    """ This is a simple tool that will subtract a number from another number."""
    return a - b

@mcp.tool
def multiply(a: int, b: int) -> int:
    """ This is a simple tool that will multiply two numbers together."""
    return a * b

@mcp.tool
def divide(a: int, b: int) -> float:
    """ This is a simple tool that will divide a number by another number."""
    return a / b

@mcp.tool
def greet(name: str) -> str:
    """ This is a simple tool that will greet a user by their name. """
    return f"Hello, {name}!"

@mcp.resource("resource://mcp-server-guide")
def mcp_server_guide() -> str:
    """ This is a simple resource that will return an MCP Server Guide in Markdown format."""

    resource = ""
    file_name = os.path.join(cwd, "src/files/mcp-server-guide.md")
    logger.debug(f"Opening resource from file '{file_name}'.")
    with open(file_name, "r") as file:
        resource = file.read()

    return resource

if __name__ == "__main__":
    mcp.run(transport="http", port=PORT)
