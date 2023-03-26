import pymongo, datetime
from bson.objectid import ObjectId
import website-neurosparkles.helpers as helpers


def connect():
    client, database = helpers.connect_db()
    return database.moods


def create(user_id, mood):
    collection = connect()
    time = datetime.datetime.utcnow().isoformat()
    collection.insert_one({'user_id': ObjectId(user_id), 'mood': int(mood), 'time': str(time)})


def read(user_id):
    collection = connect()
    return collection.find({'user_id': ObjectId(user_id)})


def read_one(mood_id):
    collection = connect()
    return collection.find_one({'_id': ObjectId(mood_id)})


def delete(mood_id):
    collection = connect()
    return collection.delete_one({'_id': ObjectId(mood_id)})
