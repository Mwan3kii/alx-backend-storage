#!/usr/bin/env python3
from pymongo.collection import Collection
from typing import Any


def insert_school(mongo_collection: Collection, **kwargs: Any) -> str:
    """
    Inserts a new document into a MongoDB collection with the given keyword argumen
    """
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)