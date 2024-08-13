#!/usr/bin/env python3
from pymongo import MongoClient

def main():
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Count total number of documents
    total_logs = collection.count_documents({})

    # Count documents by method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        method_counts[method] = collection.count_documents({"method": method})

    # Count documents with method=GET and path=/status
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})