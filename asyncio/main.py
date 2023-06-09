import asyncio
import api


async def send_data(to: str):
    print(f"Sending data to {to}")
    await asyncio.sleep(2)
    print(f"Data sent to {to}")


async def kill_time(num):
    print("Running:", num)
    await asyncio.sleep(2)
    print("Finished:", num)


async def main():
    print("Started!")
    list_of_tasks = []
    for i in range(1, 1000 + 1):
        list_of_tasks.append(kill_time(i))

    await asyncio.sleep(2)
    await asyncio.gather(*list_of_tasks)

    print("Done!")


if __name__ == "__main__":
    asyncio.run(main())
