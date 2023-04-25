from flask import Blueprint, render_template, request, session, redirect, url_for
import website.helpers as helpers
import website.errors as errors
import website.models.users as users_model
import website.models.moods as moods_model


api = Blueprint('api', __name__)


@api.route('/api/moods', methods = ['GET', 'POST'])
def moods():
    if request.method == 'GET':
        if not helpers.is_loggedin(): raise errors.NotLoggedInError()

        user = users_model.read_one(session['username'])
        moods = moods_model.read(user['_id'])
        return moods

    if request.method == 'POST':
        if not helpers.is_loggedin(): raise


@api.route('/api/sleep', methods = ['GET', 'POST'])
def sleep():
    pass


@api.route('/api/exercise', methods = ['GET', 'POST'])
def exercise():
    pass


@api.route('/api/food', methods = ['GET', 'POST'])
def food():
    pass


@api.route('/api/blood_pressure', methods = ['GET', 'POST'])
def blood_pressure():
    pass


@api.route('/api/spo2', methods = ['GET', 'POST'])
def spo2():
    pass


@api.route('/api/bpm', methods = ['GET', 'POST'])
def bpm():
    pass
