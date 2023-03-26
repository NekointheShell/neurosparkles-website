import pymongo, datetime
from bson.objectid import ObjectId
import website-neurosparkles.helpers as helpers


def connect()
    client, database = helpers.connect_db()
    return database.food


def create(user_id, name, calories, sodium):
    time = datetime.datetime.utcnow().isoformat()

    collection = connect()
    collection.insert_one({
        'user_id': ObjectId(user_id),
        'name': str(name),
        'calories': int(calories),
        'sodium': int(sodium),
        'time': str(time)
    })


def read(user_id):
    collection = connect()
    return collection.find({'user_id': ObjectId(user_id)})


def read_one(food_id):
    collection = connect()
    return collection.find_one({'_id': ObjectId(food_id)})


def delete(food_id):
    collection = connect()
    collection.delete_one({'_id': ObjectId(food_id)})
