# HTTPX vs Requests vs AIOHTTP

[![Oxylabs promo code](https://user-images.githubusercontent.com/129506779/250792357-8289e25e-9c36-4dc0-a5e2-2706db797bb5.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

[HTTPX](https://www.python-httpx.org/) is a modern HTTP client for Python that aims to provide a more enjoyable and powerful experience for making HTTP requests. It was created to add support for asynchronous programming and has quickly gained popularity in the Python community due to its feature-rich API and good performance. In this article, we will compare HTTPX to two other popular HTTP clients for Python: Requests and AIOHTTP.

See the full overview in our [blog post](https://oxylabs.io/blog/httpx-vs-requests-vs-aiohttp) where we delve deeper into each library.

- [How HTTPX compares to the Requests module](#how-httpx-compares-to-the-requests-module)
- [An overview of AIOHTTP](#an-overview-of-aiohttp)
- [HTTPX vs AIOHTTP](#httpx-vs-aiohttp)
- [Performance Comparison of AIOHTTP and HTTPX](#performance-comparison-of-aiohttp-and-httpx)
- [Comparison of HTTPX vs Requests vs AIOHTTP](#comparison-of-httpx-vs-requests-vs-aiohttp)
- [Conclusion](#conclusion)

## How HTTPX compares to the Requests module

See this comparison table of the key differences between the requests and httpx libraries:

| Feature         | Requests       | HTTPX  |
| :------------- | :-------------:| :-----:|
| Async compatibility | ❌         | ✅     |
| HTTP/2 support      | ❌         | ✅     |
| Automatic decoding  | ✅         | ✅     |
| Size                | ✅         | ❌     |
| Performance         | ❌         | ✅     |

Before running the below examples, open up your terminal and install the required libraries:
```bash
python -m pip install requests httpx aiohttp asyncio
```

Below are syntax differences between the two. The following code uses the Requests library to send a GET request:
```python
import requests
response = requests.get("https://example.com")
print(response.text)
```

The equivalent code uses the HTTPX library:
```python
import httpx
response = httpx.get("https://example.com")
print(response.text)
```

Alternatively, you can create an `httpx` client object and use its `get` method:
```python
client = httpx.Client()
response = httpx.get("https://example.com")
```

If you want to send a `POST` request using the requests library, use the post method instead of get as follows:
```python
response = requests.post("https://httpbin.org/post", data= {"name": "John", "age": 30})
```

The syntax using HTTPX is very similar:
```python
response = client.post("https://httpbin.org/post", data={"name": "John", "age": 30})
```

The two libraries are used almost identically in simple synchronous situations. The important difference is that HTTPX allows you to write **asynchronous** code as follows:
```python
import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://example.com")
        print(response.text)

asyncio.run(main())
```
HTTPX also includes automatic decoding of JSON and other common formats, which can save developers time and effort when working with responses that include structured data.

See the following example:
```python
import httpx
response = httpx.get("http://httpbin.org/get")
data = response.json()
print(data["headers"]["User-Agent"])
```
The site `http://httpbin.org/get` returns a JSON response.

In comparison, the requests library syntax is almost identical:
```python
import requests
response = requests.get("http://httpbin.org/get")
data = response.json()
print(data["headers"]["User-Agent"])
```
Do note that there is a new version of the HTTP protocol called HTTP/2, which provides far more efficient transport and better performance. If you want to read more about HTTP/2, see this [detailed document](https://http2-explained.haxx.se/). Importantly, HTTPX offers support for HTTP/2 while Requests doesn’t.

To utilize HTTP/2 with the HTTPX library, first, install the optional HTTP/2 component using the pip command:
```bash
pip install 'httpx[http2]'
```

Next, set the optional `http2` flag to `True` when you create an instance of the client as follows:
```python
client = httpx.Client(http2=True)
response = client.get("https://example.com")
print(response.http_version) # Prints HTTP/2
```
## An overview of AIOHTTP
Like HTTPX, AIOHTTP supports standard HTTP methods. It also includes support for cookies, redirects, and custom headers. AIOHTTP is particularly well-suited for making HTTP requests in high-concurrency environments due to its async-first design and efficient use of resources.

Here is an example of making an asynchronous `GET` request using AIOHTTP:
```python
import aiohttp
import asyncio

async def main(): 
    async with aiohttp.ClientSession() as session: 
            async with session.get("https://example.com") as response: 
                print(await response.text())

asyncio.run(main())
```

AIOHTTP also supports making asynchronous `POST` requests and other HTTP methods similarly. Here is an example of making a `POST` request with AIOHTTP:
```python
import aiohttp
import asyncio

async def main(): 
    async with aiohttp.ClientSession() as session: 
            async with session.post("http://httpbin.org/post", data={"key": "value"}) as response: 
                print(await response.text())

asyncio.run(main())
```

If you want to learn more about AIOHTTP, we highly recommend reading [Asynchronous Web Scraping with AIOHTTP](https://oxylabs.io/blog/asynchronous-web-scraping-python-aiohttp).

## HTTPX vs AIOHTTP
See the complete comparison in our [blog post](https://oxylabs.io/blog/httpx-vs-requests-vs-aiohttp#httpx-vs-aiohttp). The major differences of HTTPX and AIOHTTP can be summed up with this table:

| Feature         | HTTPX       | AIOHTTP  |
| :------------- | :-------------:| :-----:|
| Async compatibility | ✅         | ✅     |
| HTTP/2 support      | ✅         | ❌     |
| Performance         | ✅         | ✅🚀   |

## Performance Comparison of AIOHTTP and HTTPX
To compare the performance of AIOHTTP and HTTPX, we can build a simple program that sends multiple asynchronous `GET` requests to a website. Here is an example of such a program:
```python
import asyncio
import time
import httpx
import aiohttp

async def main():
    # Create clients for both the library
    httpx_client = httpx.AsyncClient()
    aiohttp_client = aiohttp.ClientSession()

    try:
        # Send 100 asynchronous GET requests using HTTPX
        start_time = time.perf_counter()
        tasks = [httpx_client.get("https://example.com") for _ in range(100)]
        await asyncio.gather(*tasks)
        end_time = time.perf_counter()
        print(f"HTTPX: {end_time - start_time:.2f} seconds")

        # Send 100 asynchronous GET requests using AIOHTTP
        start_time = time.perf_counter()
        tasks = [aiohttp_client.get("https://example.com") for _ in range(100)]
        await asyncio.gather(*tasks)
        end_time = time.perf_counter()
        print(f"AIOHTTP: {end_time - start_time:.2f} seconds")
    finally:
        # Close client sessions
        await aiohttp_client.close()
        await httpx_client.aclose()

asyncio.run(main())
```
Here are the results of running this code on a mac with an M1 processor and gigabit internet:

**HTTPX**: `1.22` seconds

**AIOHTTP**: `1.19` seconds

If we run the same code for `1000` requests, the numbers change significantly:

**HTTPX**: `10.22` seconds

**AIOHTTP**: `3.79` seconds

As we can see, AIOHTTP is faster than HTTPX in this case. However, it’s important to note that the performance difference between the two libraries may vary depending on the specific use case and hardware.

## Comparison of HTTPX vs Requests vs AIOHTTP

| Feature                   | HTTPX | Requests | AIOHTTP |
|:---------------------------|:-------:|:----------:|:---------:|
| Async compatible         | Yes   | No       | Yes     |
| Sync compatible          | Yes   | Yes      | No      |
| Automatic JSON decoding  | Yes   | Yes      | No      |
| HTTP/2 support           | Yes   | No       | No      |
| Cookies                   | Yes   | Yes      | Yes     |
| Redirects                 | Yes   | Yes      | Yes     |
| Authentication            | Yes   | Yes      | Yes     |
| Custom headers            | Yes   | Yes      | Yes     |
| Streaming responses       | No    | No       | No      |
| Size                      | Large | Smaller  | Smaller |
| Performance               | Good  | Good     | Excellent |

## Conclusion
Ultimately, the choice of an HTTP client library will depend on the specific needs of your project. Requests may be the best choice if you need a simple and easy-to-use library. If you need a more feature-rich library with async support, HTTPX could be a better fit.

It's worth noting that HTTPX and AIOHTTP are not the only options for making HTTP requests in Python. Many other libraries are available, each with its own features and trade-offs. Some other popular choices include http.client, urllib3, and httplib2.

Also, if you would like to try an all-in-one web scraping solution, check our [Web Scraper API](https://oxylabs.io/products/scraper-api/web) to gather real-time public information from most websites. Claim your **7-day free trial** and see for yourself whether it fits your needs.


