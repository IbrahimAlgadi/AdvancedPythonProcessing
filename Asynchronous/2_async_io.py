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
    Concurrent Execution

    All the tasks start at the same time, and the
    other coroutine start running and give
    control to other coroutine

    all this running in one thread and single core
    single thread and less overhead

    we use threading for workers (single core multiple threads)
    there is overhead
    for building workers

    we use asyncio for individual tasks (single core single thread)
    with web application you mostly find asyncio
    for web and api calls

    both they can achieve similar concurrency
    """
    start = time.time()

    await asyncio.gather(
        async_sleep(2),
        async_sleep(1),
        print_hello()
    )

    print("[*] Total Time: ", time.time() - start)


if __name__ == '__main__':
    # Run on One Core
    # we need event loop to run the loop
    asyncio.run(main())
