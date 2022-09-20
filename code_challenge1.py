"""
Link : https://www.youtube.com/watch?v=7LU1npoPmcg
"""
import asyncio

async def t1():
    await t2()
    print(f"My name is t1")
    await t3()

async def t2():
    print(f"My name is t2")
    #await t3()

async def t3():
    print(f"My name is t3")


asyncio.run(t1())