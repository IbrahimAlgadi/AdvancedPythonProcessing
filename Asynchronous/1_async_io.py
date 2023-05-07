import asyncio
import time


async def async_sleep():
    """
    Await asyncio sleep co-routine
    """
    print("[*] Before Sleep")
    await asyncio.sleep(5)
    print("[*] After Sleep")


async def print_hello():
    print("Hello")


async def main():
    await async_sleep()
    await print_hello()


if __name__ == '__main__':
    # Run on One Core
    # we need event loop to run the loop
    asyncio.run(main())
