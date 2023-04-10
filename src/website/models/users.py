import pymongo, argon2
import website.helpers as helpers


def connect():
    client, database = helpers.connect_db()
    return database.users


def create(email, password, display_name):
    helpers.validate_email(email)

    hasher = argon2.PasswordHasher()
    hash = hasher.hash(password)

    collection = connect()
    collection.insert_one({
        'email': str(email),
        'password': str(hash),
        'display_name': str(display_name)
    })


def read():
    return connect().find()


def read_one(email):
    helpers.validate_email(email)
    return connect().find_one({'email': str(email)})


def update_email(old_email, new_email):
    helpers.validate_email(old_email)
    helpers.validate_email(new_email)
    connect().update_one({'email': str(old_email)}, {'$set': {'email': str(new_email)}})


def update_password(email, password):
    helpers.validate_email(email)

    hasher = argon2.PasswordHasher()
    hash = hasher.hash(password)
    connect().update_one({'email': str(email)}, {'$set': {'password': str(hash)}})


def update_display_name(email, display_name):
    helpers.validate_email(email)
    connect().update_one({'email': str(email)}, {'$set': {'display_name': str(display_name)}})


def delete(email):
    helpers.validate_email(email)
    connect().delete_one({'email': str(email)})
