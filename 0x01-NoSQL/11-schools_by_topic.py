#!/usr/bin/env python3
"""returns list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns list of school documents containing specified topic"""
    return mongo_collection.find({ "topics": topic })