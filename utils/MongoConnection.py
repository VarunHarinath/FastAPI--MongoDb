from pymongo.mongo_client import MongoClient

def mongo_db_connection(URI):
    client = MongoClient(URI)
    try:
        client.admin.command('ping')
        print('Connected to MongoDB')
    except Exception as e:
        print(e)
