import pymongo, datetime
from bson.objectid import ObjectId
import website-neurosparkles.helpers as helpers


def connect():
    client, database = helpers.connect_db()
    return database.blood_pressure


def create(user_id, systolic, diastolic):
    time = datetime.datetime.utcnow().isoformat()

    collection = connect()
    collection.insert_one({
        'user_id': ObjectId(user_id),
        'systolic': int(systolic),
        'diastolic': int(diastolic),
        'time': str(time)
    })


def read(user_id):
    collection = connect()
    return collection.find({'user_id': ObjectId(user_id)})


def read_one(blood_pressure_id):
    collection = connect()
    return collection.find_one({'_id': ObjectId(blood_pressure_id)})


def delete(blood_pressure_id):
    collection = connect()
    collection.delete_one({'_id': ObjectId(blood_pressure_id)})
