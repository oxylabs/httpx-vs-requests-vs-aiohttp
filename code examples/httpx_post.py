import httpx
client = httpx.Client()
response = client.post("https://httpbin.org/post", data={"name": "John", "age": 30})
print(response.text)