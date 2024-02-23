import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://example.com")
        print(response.text)

asyncio.run(main())