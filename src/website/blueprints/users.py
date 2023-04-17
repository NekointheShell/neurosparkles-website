from flask import Blueprint, render_template, request, session, redirect, url_for
import website.helpers as helpers
import website.errors as errors
import website.models.users as users_model
import argon2


users = Blueprint('users', __name__)


# @users.route('/users/signup', methods = ['GET', 'POST'])
# def signup():
#     if request.method == 'GET':
#         return render_template('pages/users/signup.html')
# 
#     elif request.method == 'POST':
#         if not 'username' in request.form: raise errors.FormNotValidError()
#         if not 'email' in request.form: raise errors.FormNotValidError()
#         if not 'display_name' in request.form: raise errors.FormNotValidError()
# 
#         username = request.form['username']
#         email = request.form['email']
#         display_name = request.form['display_name']
# 
#         if not username.isalnum(): raise errors.InvalidInputError()
#         if not display_name.isalnum(): raise errors.InvalidInputError()
#         helpers.validate_email(email)
# 
#         if users_model.read_one(str(username)) != None: raise errors.DuplicateUserError()
# 
#         users_model.create(username, email, display_name)
#         return render_template('pages/users/signup_success.html')


@users.route('/users/signup')
def signup():
    return '', 404


@users.route('/users/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('pages/users/login.html')

    elif request.method == 'POST':
        if not 'username' in request.form: raise errors.FormNotValidError()
        if not 'password' in request.form: raise errors.FormNotValidError()

        username = request.form['username']
        password = request.form['password']

        attempted_user = users_model.read_one(username)

        if helpers.verify_password(password, attempted_user['password']):
            session['username'] = attempted_user['username']
            session['role'] = attempted_user['role']
            return redirect(url_for('root'))

        else: raise errors.FailedLoginError(attempted_user['username'])


@users.route('/users/logout')
def logout():
    session.clear()
    return redirect(url_for('root'))


@users.route('/users/profile', methods = ['GET', 'POST'])
def profile():
    if request.method == 'GET':
        if not helpers.is_loggedin(): raise errors.NotLoggedInError()

        user = users_model.read_one(session['username'])
        return render_template('pages/users/profile.html', user = user)

    elif request.method == 'POST':
        if not 'username' in request.form: raise errors.FormNotValidError()
        if not 'email' in request.form: raise errors.FormNotValidError()
        if not 'display_name' in request.form: raise errors.FormNotValidError()

        username = request.form['username']
        email = request.form['email']
        display_name = request.form['display_name']

        if not username.isalnum(): raise errors.InvalidInputError()
        if not display_name.isalnum(): raise errors.InvalidInputError()
        helpers.validate_email(email)

        if users_model.read_one(str(username)) != None: raise errors.DuplicateUserError()

        user = users_model.read_one(str(session['username']))
        users_model.update(
            user['username'],
            username = username,
            email = email,
            display_name = display_name
        )

        return redirect(url_for('users.profile'))


@users.route('/users/providers')
def providers():
    user = users_model.read_one(session['username'])
    return render_template('pages/users/providers.html', providers = user['providers'])


@users.route('/users/patients')
def patients():
    user = users_model.read_one(session['username'])
    return render_template('pages/users/patients.html', providers = user['patients'])


@users.route('/users/reset_password', methods = ['GET', 'POST'])
def reset_password():
    if request.method == 'GET':
        if not helpers.is_loggedin(): raise errors.NotLoggedInError()
        return render_template('pages/users/reset_password.html')

    elif request.method == 'POST':
        if not helpers.is_loggedin(): raise errors.NotLoggedInError()
        if not 'old_password' in request.form: raise errors.FormNotValidError()
        if not 'new_password' in request.form: raise errors.FormNotValidError()
        user = users_model.read_one(session['username'])

        if helpers.verify_password(request.form['old_password'], user['password']):
            users_model.update(user['username'], new_password = request.form['new_password'])
        else: raise WrongPasswordError(session['username'])

        return redirect(url_for('users.reset_password'))
