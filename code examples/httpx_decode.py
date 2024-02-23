import httpx
response = httpx.get("http://httpbin.org/get")
data = response.json()
print(data["headers"]["User-Agent"])