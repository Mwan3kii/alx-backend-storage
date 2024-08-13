#!/usr/bin/env python3
"""Improve 12-log_stats.py"""
from pymongo import MongoClient


def print_nginx_stats():
    """adding top 10 of most present IPs in collection nginx of database logs"""
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print("Methods:")
    for method in methods:
        method_count = nginx_collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")
    status_check_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{status_check_count} status check")

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
