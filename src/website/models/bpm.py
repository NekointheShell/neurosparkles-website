import pymongo, datetime
from bson.objectid import ObjectId
import website-neurosparkles.helpers as helpers


def connect():
    client, database = helpers.connect_db()
    return database.bpm


def create(user_id, beats):
    time = datetime.datetime.utcnow().isoformat()

    collection = connect()
    collection.insert_one({'user_id': ObjectId(user_id), 'beats': int(beats), 'time': str(time)})


def read(user_id):
    collection = connect()
    return collection.find({'user_id': ObjectId(user_id)})


def read_one(bpm_id):
    collection = connect()
    return collection.find_one({'_id': ObjectId(bpm_id)})


def delete(bpm_id):
    collection = connect()
    collection.delete_one({'_id': ObjectId(bpm_id)})
