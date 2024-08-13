#!/usr/bin/env python3
""" 102-log_stats """

from pymongo import MongoClient

def print_nginx_stats():
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # Count total number of documents
    total_logs = nginx_collection.count_documents({})

    print(f"{total_logs} logs")

    # Count the number of documents for each method
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")

    # Count the number of documents with method=GET and path=/status
    status_check_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_check_count} status check")

    # Aggregate IP addresses to count occurrences
    pipeline = [
        {
            '$group': {
                '_id': '$ip',
                'count': {'$sum': 1}
            }
        },
        {
            '$sort': {
                'count': -1
            }
        },
        {
            '$limit': 10
        }
    ]
    ip_counts = list(nginx_collection.aggregate(pipeline))

    print("IPs:")
    for ip in ip_counts:
        print(f"\t{ip['_id']}: {ip['count']}")

if __name__ == "__main__":
    print_nginx_stats()