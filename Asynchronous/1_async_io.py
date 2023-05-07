import asyncio
import time


async def async_sleep():
    """
    Await asyncio sleep co-routine
    """
    await asyncio.sleep(5)


async def main():
    await async_sleep()


if __name__ == '__main__':
    # Run on One Core
    # we need event loop to run the loop
    asyncio.run(main())
