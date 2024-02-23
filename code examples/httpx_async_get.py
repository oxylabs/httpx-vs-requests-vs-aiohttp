import aiohttp
import asyncio

async def main(): 
    async with aiohttp.ClientSession() as session: 
            async with session.get("https://example.com") as response: 
                print(await response.text())

asyncio.run(main())