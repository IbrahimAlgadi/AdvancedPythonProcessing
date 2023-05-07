import asyncio
import time


async def async_sleep(n):
    """
    Await asyncio sleep co-routine
    """
    print(f"[*] Before Sleep {n}")
    n = max(2, n)
    for i in range(1, n):
        yield i
        await asyncio.sleep(n)
    print(f"[*] After Sleep {n}")


async def print_hello():
    print("Hello")


async def main():
    """
    Asynchronous For Loops

    """
    start = time.time()
    async for k in async_sleep(5):
        print(k)
    print("[*] Total Time: ", time.time() - start)


if __name__ == '__main__':
    # Run on One Core
    # we need event loop to run the loop
    asyncio.run(main())
