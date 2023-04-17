from flask import Blueprint, render_template, request, session, redirect, url_for
import website.helpers as helpers
import website.errors as errors


metrics = Blueprint('metrics', __name__)


@metrics.route('/metrics', methods = ['GET', 'POST'])
def all_metrics():
    if request.method == 'GET':
        return render_template('pages/metrics.html')
