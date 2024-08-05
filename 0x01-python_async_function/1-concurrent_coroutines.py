#!/usr/bin/env python3
"""
Lets execute multiple coroutines at the same time
with async
"""
import asyncio
from asyncio.tasks import Task
from typing import  List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    takes in 2 int arguments (in this order): n
    and max_delay. You will spawn wait_random n times
    with the specified max_delay.
    """
    results: List[float] = []

    tasks: List[Task] = [asyncio
                         .create_task(wait_random(max_delay))
                         for _ in range(n)]
    for cor in asyncio.as_completed(tasks):
        res = await cor
        results.append(res)
    return results
