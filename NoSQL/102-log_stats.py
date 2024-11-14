#!/usr/bin/env python3
// Prints statistics from the nginx collection
from pymongo import MongoClient

// Lista de métodos HTTP a verificar
METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]

def log_stats(mongo_collection):
    // Script that provides some stats about Nginx logs stored in MongoDB
    
    // Obtenemos el total de registros en la colección
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    // Mostramos estadísticas por cada método HTTP
    print("Methods:")
    for method in METHODS:
        method_count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")
    
    // Contamos cuántos registros tienen el path "/status"
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")

    // Mostramos las 10 IPs más solicitadas
    print("IPs:")
    ip_counts = mongo_collection.aggregate(
        [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},  // Agrupamos por IP y contamos
            {"$sort": {"count": -1}},  // Ordenamos de mayor a menor
            {"$limit": 10}  // Limitar a las 10 IPs más frecuentes
        ]
    )
    for data in ip_counts:
        print(f"\t{data['_id']}: {data['count']}")

if __name__ == "__main__":
    // Conectamos a MongoDB y accedemos a la colección 'nginx' en la base de datos 'logs'
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    
    // Llamamos a la función que imprimirá las estadísticas
    log_stats(nginx_collection)
