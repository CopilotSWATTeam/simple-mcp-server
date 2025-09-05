
import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_resource(name: str):
    async with client:
        result = await client.read_resource("resource://mcp-server-guide")
        print(result)

asyncio.run(call_resource(""))
