import asyncio

"""
Prior Python 3.4, it was necessary to explicitly set and control the Event Loop with AsyncIO
"""


async def do_io():
    print("io start")
    await asyncio.sleep(2)
    print("io end")


async def do_other_things():
    print("doing other things")


def main() -> None:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_io())
    loop.run_until_complete(do_other_things())
    loop.close()


if __name__ == "__main__":
    main()
