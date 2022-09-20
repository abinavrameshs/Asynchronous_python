"""
Link : https://www.youtube.com/watch?v=7LU1npoPmcg
"""

import asyncio

async def fetch_data():
    print("running fetch data")
    await asyncio.sleep(6)
    return {"data" : 100} 

async def countdown():
    print("running countdown")
    for i in range(10,0,-1):
        await asyncio.sleep(2)
        print(i)

async def main():
    a = asyncio.create_task(fetch_data())
    b = asyncio.create_task(countdown())
    print(await a )
    await b

asyncio.run(main())