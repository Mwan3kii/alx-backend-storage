#!/usr/bin/env python3


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of school documents that contain the specified topic.
    """
    return mongo_collection.find({ "topics": topic })