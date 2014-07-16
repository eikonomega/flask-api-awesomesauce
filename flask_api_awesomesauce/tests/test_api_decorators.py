from base64 import b64encode

import pytest
from flask import Flask, jsonify

from flask_authorization_panda import basic_auth


@pytest.fixture
def flask_app():
    app = Flask(__name__)
    app.config['TESTING'] = True

    @app.route('/')
    @basic_auth
    def hello_world():
        return jsonify({"statusCode": 200, "message": "Ok"})

    return app

def test_no_credentials_in_application_config(flask_app):
    response = flask_app.test_client().get('/', headers={
        'Authorization': 'Basic {}'.format(b64encode('admin:secret'))})
    assert '500' in response.data


def test_no_credentials_in_request(flask_app):
    flask_app.config['basic_auth_credentials'] = dict(username='admin',
                                                      password='secret')
    response = flask_app.test_client().get('/')
    assert "HTTP Basic Auth required for this URL" in response.data
    assert "WWW-Authenticate" in response.headers


def test_basic_auth_with_bad_credentials(flask_app):
    flask_app.config['basic_auth_credentials'] = dict(username='admin',
                                                      password='secret')
    response = flask_app.test_client().get('/', headers={
        'Authorization': 'Basic {}'.format(b64encode('wrong:creds'))})
    assert 'with proper credentials' in response.data
    assert "WWW-Authenticate" in response.headers


def test_basic_auth(flask_app):
    flask_app.config['basic_auth_credentials'] = dict(username='admin',
                                                      password='secret')
    response = flask_app.test_client().get('/', headers={
        'Authorization': 'Basic {}'.format(b64encode('admin:secret'))})
    assert '200' in response.data





