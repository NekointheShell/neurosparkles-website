import pymongo, datetime
from bson.objectid import ObjectId
import website-neurosparkles.helpers as helpers


def connect():
    client, database = helpers.connect_db()
    return database.spo2


def create(user_id, level):
    time = datetime.datetime.utcnow().isoformat()

    collection = connect()
    collection.insert_one({'user_id': ObjectId(user_id), 'level': int(level), 'time': str(time)})


def read(user_id):
    collection = connect()
    return collection.find({'user_id': ObjectId(user_id)})


def read_one(spo2_id):
    collection = connect()
    return collection.find_one({'_id': ObjectId(spo2_id)})


def delete(spo2_id):
    collection = connect()
    collection = delete_one({'_id': ObjectId(spo2_id)})
