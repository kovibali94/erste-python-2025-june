import asyncio
import aiohttp


async def http_request(url):
    async with aiohttp.ClientSession() as session:
        return await session.get(url)


async def get_http_request_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main():
    # V1
    # response = await http_request("https://jsonplaceholder.typicode.com/posts")
    # print(response, type(response))
    # data = await response.json()
    # print(data, type(data))

    # V2
    # response = await get_http_request_json("https://jsonplaceholder.typicode.com/posts")
    # print(response, type(response))

    # V3
    urls = [
        "https://jsonplaceholder.typicode.com/posts",
        "https://jsonplaceholder.typicode.com/comments",
        "https://jsonplaceholder.typicode.com/albums",
    ]

    tasks = [get_http_request_json(url) for url in urls]
    responses = await asyncio.gather(*tasks)
    print(responses)


if __name__ == "__main__":
    asyncio.run(main())
