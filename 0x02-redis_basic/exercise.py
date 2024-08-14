#!/usr/bin/env python3
"""Import redis"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that counts the number of times a method is called."""
    
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Use the method's qualified name as the key
        key = method.__qualname__
        
        # Increment the count for this method in Redis
        self._redis.incr(key)
        
        # Call the original method and return its result
        return method(self, *args, **kwargs)
    
    return wrapper


class Cache:
    def __init__(self):
        # Initialize Redis client and flush the database
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate a random key using uuid
        random_key = str(uuid.uuid4())
        # Store the data in Redis with the generated key
        self._redis.set(random_key, data)
        # Return the generated key
        return random_key
    
    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        # Retrieve data from Redis
        data = self._redis.get(key)
        
        # If the data exists and a function is provided, apply the function
        if data is not None and fn is not None:
            return fn(data)
        
        # If the data exists and no function is provided, return it as is
        return data

    def get_str(self, key: str) -> Optional[str]:
        # Retrieve the data and decode it as a UTF-8 string
        data = self.get(key, fn=lambda d: d.decode('utf-8'))
        return data

    def get_int(self, key: str) -> Optional[int]:
        # Retrieve the data and convert it to an integer
        data = self.get(key, fn=int)
        return data
    
