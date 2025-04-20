import asyncio
import time


async def task(name):
    print(f"Starting task {name}")
    await asyncio.sleep(2)  # Simulates an async I/O operation
    print(f"Finished task {name}")


# Run tasks concurrently using asyncio
async def main():
    start = time.time()

    # Schedule both tasks concurrently
    await asyncio.gather(task("A"), task("B"))

    end = time.time()
    print(f"Total time: {end - start:.2f} seconds")


# Run the asyncio event loop
asyncio.run(main())
