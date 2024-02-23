import requests
response = requests.post("https://httpbin.org/post", data= {"name": "John", "age": 30})
print(response.text)
