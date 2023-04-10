import pymongo, os
import string
import validators


def connect_db():
    client = pymongo.MongoClient(os.environ['MONGO_URL'])
    database = client.neurosparkles

    return client, database


def validate_email(email):
    try:
        validators.email(email)
        return True

    except ValidationFailure:
        raise Exception('Invalid email: {}'.format(email)
