#!/usr/bin/env python3
"""
import async_comprehension from the previous file and write
a measure_runtime coroutine that will
execute async_comprehension four times in
parallel using asyncio.gather
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime of parallel async execution coroutines
    """
    start = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    stop = time.perf_counter()
    return stop - start
