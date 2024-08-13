from pymongo.collection import Collection
from typing import Any

def insert_school(mongo_collection: Collection, **kwargs: Any) -> str:
    """
    Inserts a new document into a MongoDB collection with the given keyword arguments.

    Parameters:
    mongo_collection (Collection): The pymongo collection object.
    **kwargs: The document fields and values.

    Returns:
    str: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return str(result.inserted_id)