#!/usr/bin/env python3
"""Import modules needed"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that counts the number of times a method is called."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Use the method's qualified name as the key"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a function."""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """store the history of inputs and outputs"""
        method_name = method.__qualname__
        self._redis.rpush(f"{method_name}:inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{method_name}:outputs", str(output))
        return output

    return wrapper


def replay(method: Callable):
    """Displays the history of calls of a particular function."""
    method_key = method.__qualname__
    inputs, outputs = method_key + ':inputs', method_key + ':outputs'
    redis = method.__self__._redis
    method_count = redis.get(method_key).decode('utf-8')
    print(f'{method_key} was called {method_count} times:')
    IOTuple = zip(redis.lrange(inputs, 0, -1), redis.lrange(outputs, 0, -1))
    for inp, outp in list(IOTuple):
        attr, data = inp.decode("utf-8"), outp.decode("utf-8")
        print(f'{method_key}(*{attr}) -> {data}')


class Cache:
    def __init__(self):
        """Initialize Redis client and flush the database"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """takes a data argument and returns a string."""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """Retrieve data from Redis"""
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve the data and decode it as a UTF-8 string"""
        data = self.get(key, fn=lambda d: d.decode('utf-8'))
        return data

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve the data and convert it to an integer"""
        data = self.get(key, fn=int)
        return data
