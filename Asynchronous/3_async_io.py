import asyncio
import time


async def async_sleep(n):
    """
    Await asyncio sleep co-routine
    """
    print(f"[*] Before Sleep {n}")
    await asyncio.sleep(n)
    print(f"[*] After Sleep {n}")


async def print_hello():
    print("Hello")


async def main():
    """
    Timeout

    waiting for coroutine to finish sometimes
    taskes long time
    like server hangs because of overloading
    then we need to use timeout to regain control
    over the system

    """
    start = time.time()

    try:
        await asyncio.gather(
            asyncio.wait_for(async_sleep(2), 1),
            async_sleep(1),
            print_hello()
        )
    except asyncio.TimeoutError:
        print("[*] Encountered Timeout Error...")

    print("[*] Total Time: ", time.time() - start)


if __name__ == '__main__':
    # Run on One Core
    # we need event loop to run the loop
    asyncio.run(main())
