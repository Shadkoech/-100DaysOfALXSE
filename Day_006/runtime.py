#!/usr/bin/env python3
""" Python module that showcases the use of an Async Generator"""

import asyncio
import random
import time
from typing import Generator
from typing import List


async def async_generator() -> Generator[float, None, None]:
    """ Coroutine that yields random numbers asynchronously.
    Loops 10 times, each time asynchronously waiting 1 second,
    then yielding a random number between 0 and 10.
    Returns:
        AsyncGenerator: An asynchronous generator. """

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    Returns:
        list: A list of 10 random numbers."""

    # Collect 10 random numbers using async comprehension over async_generator
    random_numbers = [num async for num in async_generator()]

    return random_numbers

async def measure_runtime() -> float:
    """Coroutine measuring total runtime of executing async_comprehension
    four times in parallel using asyncio.gather.
    Returns:
        float: Total runtime in seconds.
    """

    # Record the starting time
    start_time = time.time()
    # Execute async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end_time = time.time()

    # Calculate the total runtime
    total_runtime = end_time - start_time

    return total_runtime

