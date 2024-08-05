#!/usr/bin/env python3
"""
Measuring the runtime of a function
"""
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n
import asyncio


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the runtime of wait_n function
    """
    start: float = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    stop: float = perf_counter()
    duration: float = stop - start
    return duration / n
