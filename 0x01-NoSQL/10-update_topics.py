#!/usr/bin/env python3


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of a school document with the given name
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )