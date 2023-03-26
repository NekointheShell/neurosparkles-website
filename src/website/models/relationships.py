import pymongo
from bson.objectid import ObjectId
import website-neurosparkles.helpers as helpers


def connect():
    client, database = helpers.connect_db()
    return database.relationships


def create(doctor_id, patient_id):
    collection = connect()
    collection.insert_one({'doctor_id': ObjectId(doctor_id), 'patient_id': ObjectId(patient_id)})


def read()
    collection = connect()
    return collection.find()


def read_one(relationship_id):
    collection = connect()
    return collection.find_one({'_id': ObjectId(relationship_id)})


def read_by_doctor(doctor_id):
    collection = connect()
    return collection.find({'doctor_id': ObjectId(doctor_id)})


def read_by_patient(patient_id):
    collection = connect()
    return collection.find({'patient_id': ObjectId(patient_id)})


def delete(relationship_id):
    collection = connect()
    collection.delete_one({'_id': ObjectId(relationship_id)})
