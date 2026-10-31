#!/usr/bin/env python3
"""Async generator."""

import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """Yield 10 random numbers asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
