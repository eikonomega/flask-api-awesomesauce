import json

import pytest
from flask import Flask, jsonify

from flask_api_awesomesauce.api_decorators import (
    api_declaration, json_response)


@pytest.fixture
def flask_app():
    app = Flask(__name__)
    app.config['TESTING'] = True

    @app.route('/', methods=['GET'])
    @api_declaration('1.0')
    def basic_get_request():
        return json_response(200, "Ok")

    @app.route('/test-url-parameters', methods=['GET'])
    @api_declaration('1.0', required_url_parameters={
        "test_url_parameters": "Misc Value"})
    def parameterized_get_request():
        return json_response(200, "Ok")

    @app.route('/test-post', methods=['POST'])
    @api_declaration('1.0', required_payload_elements={
        "test_element": "This is just a description"})
    def json_post_request():
        return json_response(201, "Ok")

    return app


def test_api_declaration_with_no_optional_parameters(flask_app):
    """
    Unknown

    """
    response = json.loads(flask_app.test_client().get('/').get_data())
    assert all([response['message'] == 'Ok', response['statusCode'] == 200])


def test_api_declaration_with_missing_invalid_json_payload(flask_app):
    """
    Unknown

    """
    response = flask_app.test_client().post(
        '/test-post',
        content_type='application/json',
        data="{'body': }")

    response = json.loads(response.get_data())
    assert all([
        response['message'] == 'JSON request payload has a syntax error(s).',
        response['statusCode'] == 400,
        response['usage']])


def test_api_declaration_with_missing_required_json_element(flask_app):
    """
    Unknown

    """
    response = flask_app.test_client().post(
        '/test-post',
        content_type='application/json',
        data=json.dumps({'body': 'body of the blog post'}))

    response = json.loads(response.get_data())
    assert all([
        response['message'] == 'JSON is missing a required element(s).',
        response['statusCode'] == 400,
        response['usage']])


def test_api_declaration_with_missing_required_url_parameter(flask_app):
    """
    Unknown

    """
    response = flask_app.test_client().get(
        '/test-url-parameters')

    response = json.loads(response.get_data())
    print(response)
    assert all([
        response['message'] == 'A required URL parameter(s) is missing.',
        response['statusCode'] == 400,
        response['usage']])





