#!/usr/bin/env python3
from pymongo.collection import Collection
from typing import List


def update_topics(mongo_collection: Collection, name: str, topics: List[str]) -> None:
    """
    Updates the 'topics' field of a school document with the given name
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )