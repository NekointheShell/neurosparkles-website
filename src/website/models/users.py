import pymongo, argon2
from bson.objectid import ObjectId
import website-neurosparkles.helpers as helpers


def connect():
    client, database = helpers.connect_db()
    return database.users


def create(email, password, display_name):
    hasher = argon2.PasswordHasher()
    hash = hasher.hash(password)

    collection = connect()
    collection.insert_one({
        'email': str(email),
        'password': str(hash),
        'display_name': str(display_name)
    })


def read():
    collection = connect()
    return collection.find()


def read_one(user_id):
    collection = connect()
    return collection.find_one({'_id': ObjectId(user_id)})


def update_email(user_id, email):
    collection = connect()
    collection.update_one({'_id': ObjectId(user_id)}, {'$set': {'email': str(email)}})


def update_password(user_id, password):
    hasher = argon2.PasswordHasher()
    hash = hasher.hash(password)

    collection = connect()
    collection.update_one({'_id': ObjectId(user_id)}, {'$set': {'password': str(hash)}})


def update_display_name(user_id, display_name):
    collection = connect()
    collection.update_one(
        {'_id': ObjectId(user_id)},
        {'$set': {'display_name': str(display_name)}}
    )


def delete(user_id):
    collection = connect()
    collection.delete_one({'_id': ObjectId(user_id)})
