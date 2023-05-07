import asyncio
import time


async def async_sleep(n):
    """
    Await asyncio sleep co-routine
    """
    print(f"[*] Before Sleep {n}")
    await asyncio.sleep(5)
    print(f"[*] After Sleep {n}")


async def print_hello():
    print("Hello")


async def main():
    start = time.time()

    task = asyncio.create_task(async_sleep(1))
    await async_sleep(2)
    await print_hello()
    await task

    print("[*] Total Time: ", time.time() - start)


if __name__ == '__main__':
    # Run on One Core
    # we need event loop to run the loop
    asyncio.run(main())
