import asyncio
from time import perf_counter


async def get_http_request():
    print("Starting GET HTTP request...")
    await asyncio.sleep(2)
    print("HTTP request completed.")
    return "Response data"


async def post_http_request(data):
    print(f"Starting POST HTTP request..., data: {data}")
    await asyncio.sleep(2)
    print("HTTP request completed.")
    return "Response data"


# async def main():
#     print("Starting main function...")
#     get_response = await get_http_request()
#     post_response = await post_http_request("Johnny")
#     print(f"GET Response: {get_response}")
#     print(f"POST Response: {post_response}")
#     print("Main function completed.")

async def main():
    print("Starting main function...")
    get = asyncio.create_task(get_http_request())
    post = asyncio.create_task(post_http_request("Johnny"))
    await get, post
    print("Main function completed.")


if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(main())
    end = perf_counter()
    print(f"Time taken: {end - start:.4f} seconds")
