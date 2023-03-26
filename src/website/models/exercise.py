import pymongo, datetime
from bson.objectid import ObjectId
import website-neurosparkles.helpers as helpers


def connect():
    client, database = helpers.connect_db()
    return database.exercise


def create(user_id, start_time, stop_time):
    collection = connect()
    collection.insert_one({
        'user_id': ObjectId(user_id),
        'start_time': str(start_time),
        'stop_time': str(stop_time)
    })


def read(user_id):
    collection = connect()
    return collection.find({'user_id': ObjectId(user_id)})


def read_one(exercise_id):
    collection = connect()
    return collection.find_one({'_id': ObjectId(exercise_id)})


def delete(exercise_id):
    collection = connect()
    collection.delete_one({'_id': ObjectId(exercise_id)})
