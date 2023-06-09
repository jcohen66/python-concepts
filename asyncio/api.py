import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2.5)
    print("Data fetched!")
    
    return 'API Data'