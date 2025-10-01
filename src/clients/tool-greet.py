import asyncio
import sys

from fastmcp import Client

if len(sys.argv) > 1:
    name = sys.argv[1] 
else:
    name = "World"

client = Client("http://localhost:8000/mcp")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool("greet", {"name": name})
        print(result)

asyncio.run(call_tool(name))
