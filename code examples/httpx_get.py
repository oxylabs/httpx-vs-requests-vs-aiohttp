import httpx
response = httpx.get("https://example.com")
print(response.text)