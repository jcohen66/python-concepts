import asyncio
import api


async def main():
    task = asyncio.create_task(api.fetch_data())
    # task.cancel()

    # await asyncio.sleep(3)

    try:
        # if task.done():
        #     print(task.result)
        # result = await task
        # print(result)

        await asyncio.wait_for(task, timeout=2)
    except asyncio.CancelledError as e:
        print("CANCELLED: Request was cancelled...")
    except asyncio.TimeoutError as e:
        print("TIMEDOUT: Request took too long...")


if __name__ == "__main__":
    asyncio.run(main())
