import asyncio


async def http_request():
    print("Starting HTTP request...")
    await asyncio.sleep(2)
    print("HTTP request completed.")
    return "Response data"


async def main():
    print(f"Get:  {await http_request()}")


if __name__ == "__main__":
    print("Starting main function...")
    asyncio.run(main())
    print("Main function completed.")
