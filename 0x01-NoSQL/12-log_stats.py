#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == '__main__':
    con = MongoClient('mongodb://localhost:27017')
    collection = con.logs.nginx

    print(f'{collection.estimated_document_count()} logs')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')

    for req in methods:
        print('\tmethods {}: {}'.format(req,
              collection.count_documents({'method': req})))

    print('{} status check'.format(collection.count_documents(
          {'method': 'GET', 'path': '/status'})))
