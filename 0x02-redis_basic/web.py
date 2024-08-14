#!/usr/bin/env python3
"""Import modules needed"""
import redis
import requests
from typing import Callable
from functools import wraps

redis_client = redis.Redis()


def cache_with_expiration(method: Callable) -> Callable:
    """Decorator to cache the result of a method with an expiration time."""

    @wraps(method)
    def wrapper(url: str) -> str:
        """Generate the cache key for the URL"""
        cache_key = f"cached:{url}"
        cached_result = redis_client.get(cache_key)

        if cached_result:
            return cached_result.decode('utf-8')
        result = method(url)
        redis_client.setex(cache_key, 10, result)

        return result

    return wrapper


@cache_with_expiration
def get_page(url: str) -> str:
    """Fetch the HTML content of a URL and track access."""
    redis_client.incr(f"count:{url}")
    response = requests.get(url)
    return response.text
