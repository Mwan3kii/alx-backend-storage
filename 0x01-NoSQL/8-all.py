from typing import List, Dict
from pymongo.collection import Collection

def list_all(mongo_collection: Collection) -> List[Dict]:
    """
    List all documents in a MongoDB collection.

    Parameters:
    mongo_collection (Collection): The pymongo collection object.

    Returns:
    List[Dict]: A list of documents, or an empty list if no documents are found.
    """
    return list(mongo_collection.find())