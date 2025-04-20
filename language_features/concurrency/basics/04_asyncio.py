import asyncio
import time


async def task(name):
    print(f"Starting task {name}")
    await asyncio.sleep(2)
    print(f"Finished task {name}")


async def main():
    start = time.time()

    await asyncio.gather(task("A"), task("B"))

    end = time.time()
    print(f"Total time: {end - start:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
