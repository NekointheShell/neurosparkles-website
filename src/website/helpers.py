from flask import session

import pymongo, os, string
import validators
import argon2

import website.models.users as users_model


def connect_db():
    client = pymongo.MongoClient(os.environ['MONGO_URL'])
    database = client.neurosparkles

    return client, database


def validate_email(email):
    try:
        validators.email(email)
        return True

    except ValidationFailure:
        raise InvalidEmailError(email)


def hash_password(password):
    hasher = argon2.PasswordHasher()
    hash = hasher.hash(password)

    return hash


def verify_password(password, hash):
    hasher = argon2.PasswordHasher()
    if hasher.verify(hash, password): return True
    else: return False


def is_loggedin():
    if 'username' in session: return True
    else: return False
