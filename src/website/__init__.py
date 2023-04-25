from flask import Flask, render_template
from werkzeug.exceptions import HTTPException
import secrets


app = Flask(__name__)


@app.errorhandler(HTTPException)
def http_exception_handler(exception):
    return render_template('pages/error.html')


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('images/brain.ico')


@app.route('/')
def root():
    return render_template('pages/index.html')


@app.route('/resources')
def resources():
    return render_template('pages/resources.html')
