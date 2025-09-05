import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_resource(name: str):
    async with client:
        result = await client.list_resources()
        print(result)

asyncio.run(call_resource(""))
    
