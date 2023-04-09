from flask import Flask, render_template
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex()


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('images/brain.ico')


@app.route('/')
def root():
    return render_template('pages/index.html')


@app.route('/resources')
def resources():
    return render_template('pages/resources.html')


@app.route('/login', methods = ['GET', 'POST', 'DELETE'])
def login():
    if request.method == 'GET':
        return render_template('pages/login.html')

    elif request.method == 'POST':
        return 'pass'

    elif request.method == 'DELETE':
        return 'pass'
