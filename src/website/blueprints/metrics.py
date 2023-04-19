from flask import Blueprint, render_template, request, session, redirect, url_for
import website.helpers as helpers
import website.errors as errors
import website.models.users as users_model


metrics = Blueprint('metrics', __name__)


@metrics.route('/metrics/<username>', methods = ['GET', 'POST'])
def all_metrics(username = None):
    if not helpers.is_loggedin():
        return redirect(url_for('root'))

    if request.method == 'GET':
        if username == None or username == session['username']:
            return render_template('pages/metrics_with_forms.html', user = session['username'])

        elif username != None:
            user = users_model.read_one(session['username'])

            if username in user['patients']:
                return render_template('pages/metrics.html', user = username)
