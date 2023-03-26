import pymongo, os


def connect_db():
    client = pymongo.MongoClient(os.environ['MONGO_URL'])
    database = client.neurosparkles

    return client, database
