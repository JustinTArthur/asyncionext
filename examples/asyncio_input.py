import asyncio
import asyncionext


async def sleep_and_print():
    for i in range(5):
        await asyncio.sleep(1)
        print(i)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    sleeper = loop.create_task(sleep_and_print())
    result = loop.run_until_complete(asyncionext.input_async("Put some text in!"))
    print("Got result!: " + result)
    loop.run_until_complete(sleeper)
