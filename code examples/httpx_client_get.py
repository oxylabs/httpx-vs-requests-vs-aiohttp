import httpx
client = httpx.Client()
response = httpx.get("https://example.com")
print(response.text)