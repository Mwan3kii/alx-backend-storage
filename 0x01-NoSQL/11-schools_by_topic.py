from pymongo.collection import Collection
from typing import List, Dict

def schools_by_topic(mongo_collection: Collection, topic: str) -> List[Dict]:
    """
    Returns a list of school documents that contain the specified topic.

    Parameters:
    mongo_collection (Collection): The pymongo collection object.
    topic (str): The topic to search for in the school's topics list.

    Returns:
    List[Dict]: A list of school documents that have the specified topic.
    """
    return list(mongo_collection.find({ "topics": topic }))