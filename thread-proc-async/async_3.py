import asyncio
from time import perf_counter
import random


async def http_request(id, sec):
    # print(f"Starting HTTP request... ID: {id}")
    await asyncio.sleep(sec)
    # print(f"HTTP request completed. ID: {id}")
    return "Response data"


async def main():
    requests = [http_request(i + 1, random.randint(1, 5)) for i in range(100000)]
    await asyncio.gather(*requests)


if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(main())
    end = perf_counter()
    print(f"Time taken: {end - start:.4f} seconds")
