import aiohttp
import asyncio

async def main(): 
    async with aiohttp.ClientSession() as session: 
            async with session.post("http://httpbin.org/post", data={"key": "value"}) as response: 
                print(await response.text())

asyncio.run(main())