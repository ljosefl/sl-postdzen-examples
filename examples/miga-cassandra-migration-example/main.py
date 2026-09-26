import cassandra
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import SimpleStatement
import pandas as pd
from pymongo import MongoClient

def connect_to_cassandra():
    auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
    cluster = Cluster(['127.0.0.1'], auth_provider=auth_provider)
    session = cluster.connect('test_keyspace')
    session.execute('USE test_keyspace')
    return session

def connect_to_mongodb():
    mongo_client = MongoClient('mongodb://localhost:27017/')
    db = mongo_client['test_db']
    collection = db['test_collection']
    return collection

def migrate_data(session, collection):
    rows = collection.find()
    for row in rows:
        insert_query = SimpleStatement(f"INSERT INTO test_table (key, value) VALUES ({row['_id']}, '{row['value']}')")
        session.execute(insert_query)

if __name__ == "__main__":
    session = connect_to_cassandra()
    collection = connect_to_mongodb()
    migrate_data(session, collection)