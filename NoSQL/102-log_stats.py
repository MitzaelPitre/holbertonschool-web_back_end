#!/usr/bin/env python3
"""log stats from collection
"""
from pymongo import MongoClient
from collections import Counter

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """ script that provides some stats about Nginx logs stored in MongoDB
    """
    items = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(mongo_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")
    
    # Counting IPs
    ip_counter = Counter()
    for log in mongo_collection.find():
        ip_counter[log['ip']] += 1
    
    # Sorting IPs by frequency and displaying the top 10
    print("IPs:")
    for ip, count in ip_counter.most_common(10):
        print(f"\t{ip}: {count}")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
