#!/usr/bin/env python3
""" 
Let's execute multiple coroutines at the same time with async 
"""
import asyncio
from typing import List
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ 
    Asynchronously waits for multiple random delays.
    
    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay allowed in seconds.
        
    Returns:
        List[float]: A list containing the random delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
