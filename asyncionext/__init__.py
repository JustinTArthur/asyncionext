"""
Proposed additions to the asyncio module of the Python standard library.
"""
import asyncio
import aiofiles.os


async def input_async(*args, loop=None, executor=None):
    loop = loop or asyncio.get_event_loop()
    return await loop.run_in_executor(executor, input, *args)


open = aiofiles.open
os = aiofiles.os