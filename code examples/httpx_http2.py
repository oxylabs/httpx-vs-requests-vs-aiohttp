import httpx
client = httpx.Client(http2=True)
response = client.get("https://example.com")
print(response.http_version) # Prints HTTP/2