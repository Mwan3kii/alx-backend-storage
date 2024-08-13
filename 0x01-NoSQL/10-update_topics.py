from pymongo.collection import Collection
from typing import List

def update_topics(mongo_collection: Collection, name: str, topics: List[str]) -> None:
    """
    Updates the 'topics' field of a school document with the given name.

    Parameters:
    mongo_collection (Collection): The pymongo collection object.
    name (str): The name of the school document to update.
    topics (List[str]): The list of topics to set in the 'topics' field.
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )