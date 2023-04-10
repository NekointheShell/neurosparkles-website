from flask import Blueprint, render_template, request, session, redirect, url_for
import website.models.users as users_model
import website.errors as errors
import argon2


auth = Blueprint('login', __name__)


@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('pages/login.html')

    elif request.method == 'POST':
        attempted_user = users_model.read_one(request.forms['email'])

        hasher = argon2.PasswordHasher()
        if hasher.verify(attempted_user['password'], request.forms['password']):
            session['email'] = attempted_user['email']

        else: raise FailedLoginError(attempted_user)


@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))
