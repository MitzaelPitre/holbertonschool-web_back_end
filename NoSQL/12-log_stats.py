#!/usr/bin/env python3
"""Gets stats for Nginx from MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    data = MongoClient().logs.nginx
    print(f'{data.count_documents({})} logs')
    print('    Methods:')
    print(f'        method GET: {data.count_documents({"method": "GET"})}')
    print(f'        method POST: {data.count_documents({"method": "POST"})}')
    print(f'        method PUT: {data.count_documents({"method": "PUT"})}')
    print(f'        method PATCH: {data.count_documents({"method": "PATCH"})}')
    print(f'        method DELETE: {data.count_documents({"method": "DELETE"})}')
    print(f'{data.count_documents({"method": "GET", "path": "/status"})} status check')
