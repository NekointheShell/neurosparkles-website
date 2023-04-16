import pymongo, argon2, secrets
import website.helpers as helpers
import website.errors as errors


def connect():
    client, database = helpers.connect_db()
    return database.users


def create(username, email, display_name, role = 'user'):
    random_password = secrets.token_hex()
    connect().insert_one({
        'username': str(username),
        'email': str(email),
        'display_name': str(display_name),
        'role': str(role),
        'providers': [],
        'patients': [],
        'password': str(helpers.hash_password(secrets.token_hex()))
    })


def read():
    return connect().find()


def read_one(username):
    return connect().find_one({'username': str(username)})


def update(username, new_username = None, new_email = None, new_display_name = None, new_role = None):
    if new_username != None:
        connect().update_one({'username': str(username)}, {'$set': {'username': str(username)}})

    if new_email != None:
        connect().update_one({'username': str(username)}, {'$set': {'email': str(new_email)}})

    if new_display_name != None:
        connect().update_one({'username': str(username)}, {'$set': {'display_name': str(new_display_name)}})

    if new_role != None:
        connect().update_one({'username': str(username)}, {'$set': {'role': str(role)}})


def delete(username):
    connect().delete_one({'username': str(username)})
