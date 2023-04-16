from flask import Flask, render_template
import secrets
from website.blueprints.users import users


app = Flask(__name__)
app.secret_key = secrets.token_hex()

app.register_blueprint(users)


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('images/brain.ico')


@app.route('/')
def root():
    return render_template('pages/index.html')


@app.route('/resources')
def resources():
    return render_template('pages/resources.html')
