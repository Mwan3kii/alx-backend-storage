#!/usr/bin/env python3
from pymongo.collection import Collection
from typing import List, Dict


def schools_by_topic(mongo_collection: Collection, topic: str) -> List[Dict]:
    """
    Returns a list of school documents that contain the specified topic.
    """
    return list(mongo_collection.find({ "topics": topic }))