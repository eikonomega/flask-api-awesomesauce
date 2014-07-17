"""
Decorator functions for web api methods.
"""

from functools import wraps

from flask import jsonify, request
from flask.wrappers import BadRequest

import utilities


def json_response(status_code, message, additional_data=None):
    """
    Args:
        status_code (int): HTTP Status Code for response object.
        response_data (dict): Data to be returned as JSON in the response body.

    Returns:
        A Flask Response object

    """
    response_payload = {
        'statusCode': status_code,
        'message': message
    }

    if additional_data:
        response_payload.update(additional_data)

    utilities.python_to_json_syntax(response_payload)

    response = jsonify(response_payload)
    response.status_code = status_code
    return response


def api_declaration(
        api_version,
        required_payload_elements=None,
        optional_payload_elements=None,
        required_url_parameters=None,
        optional_url_parameters=None):
    """
    Args:
        api_version (str): API version being served by app.
        required_payload_elements (dict): Names and descriptions of
            required JSON payload elements.
        optional_payload_elements (dict): Names and descriptions of
            optional JSON payload elements.
        required_url_parameters (dict): Names and descriptions of
            required URL parameters.
        optional_url_parameters (dict): Names and descriptions of
            optional URL parameters.

    """
    api_usage_declarations = {
        key: value for key, value in locals().items() if type(value) == dict}

    utilities.python_to_json_syntax(api_usage_declarations)

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            # Check for Invalid JSON.
            try:
                request_json = request.get_json()
            except BadRequest:
                return json_response(
                    400, 'JSON request payload has a syntax error(s).',
                    {'usage': api_usage_declarations})

            if 'requiredPayloadElements' in api_usage_declarations:
                for element in api_usage_declarations[
                    'requiredPayloadElements']:
                    if not element in request_json:
                        return json_response(
                            400,
                            'JSON is missing a required element(s).',
                            {'usage': api_usage_declarations})

            if 'requiredUrlParameters' in api_usage_declarations:
                request_args = request.args
                for element in api_usage_declarations['requiredUrlParameters']:
                    if not element in request_args:
                        return json_response(
                            400,
                            'A required URL parameter(s) is missing.',
                            {'usage': api_usage_declarations})

            return func(*args, **kwargs)

        return wrapper

    return decorate


# def response_template(api_version,
#                       required_payload_elements=None,
#                       optional_payload_elements=None,
#                       required_url_parameters=None,
#                       optional_url_parameters=None):
#     """
#     Ensure that a flask.Response object conforms to desired specifications.
#
#     What should this function do?
#
#     On the front side:
#         1. Verifies that the JSON in the request in valid.
#         2. Verifies that required payload/url elements are provided.
#
#     On the backside:
#         1. Only include this information if original functions response code
#         is 4xx/5xx to avoid overly verbose responses.
#
#     """
#     # Extract dictionary objects from locals().items()
#     api_usage_declarations = {
#         key: value for key, value in locals().items() if type(value) == dict}
#
#     json_syntax_api_usage_declarations = dict()
#     for key, value in api_usage_declarations.iteritems():
#         for python_syntax in re.finditer(r'_[a-z]', key):
#             key = key.replace(
#                 python_syntax.group(), python_syntax.group()[1].upper())
#         json_syntax_api_usage_declarations[key] = value
#
#     def decorate(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#
#             response_data = dict(
#                 meta=dict(apiVersion=api_version,
#                           usage=json_syntax_api_usage_declarations,
#                           request=dict(
#                               requestUrl=request.base_url,
#                               requestMethod=request.method),
#                           response=dict()))
#
#             # Check for Invalid JSON.
#             try:
#                 request.get_json()
#             except BadRequest:
#                 response_data['meta']['response']['message'] = (
#                     'JSON contains syntax errors.')
#                 response_data['meta']['response']['statusCode'] = 400
#                 response = jsonify(response_data)
#                 response.status_code = (
#                     response_data['meta']['response']['statusCode'])
#                 current_app.logger.error(
#                     response_data['meta']['response']['message'])
#                 return response
#
#             if 'requiredPayloadElements' in json_syntax_api_usage_declarations:
#                 request_json = request.get_json()
#                 for element in json_syntax_api_usage_declarations[
#                     'requiredPayloadElements']:
#                     if not element in request_json:
#                         response_data['meta']['response']['statusCode'] = 400
#                         response_data['meta']['response']['message'] = (
#                             'Required JSON element(s) are not in payload.')
#                         response = jsonify(response_data)
#                         response.status_code = (
#                             response_data['meta']['response']['statusCode'])
#                         current_app.logger.error(
#                             response_data['meta']['response']['message'])
#                         return response
#             elif 'requiredUrlParameters' in json_syntax_api_usage_declarations:
#                 request_args = request.args
#                 for element in json_syntax_api_usage_declarations[
#                     'requiredUrlParameters']:
#                     if not element in request_args:
#                         response_data['meta']['response']['statusCode'] = 400
#                         response_data['meta']['response']['message'] = (
#                             'Missing required URL parameter(s).')
#                         response = jsonify(response_data)
#                         response.status_code = (
#                             response_data['meta']['response']['statusCode'])
#                         current_app.logger.error(
#                             response_data['meta']['response']['message'])
#                         return response
#
#             original_response = func(*args, **kwargs)
#             original_response_data = json.loads(original_response.data)
#
#             if type(original_response) != Response:
#
#
#             # Reassign dict location of 'meta' elements from original response.
#             response_data['meta']['response'] = dict()
#             for meta_element in ['statusCode', 'message']:
#                 if meta_element in original_response_data:
#                     response_data['meta']['response'][meta_element] = (
#                         original_response_data[meta_element])
#                     original_response_data.pop(meta_element)
#
#             # Transfer remaining origin_response elements to new response dict.
#             for element in original_response_data:
#                 response_data[element] = original_response_data[element]
#
#             response = jsonify(response_data)
#             response.status_code = (
#                 response_data['meta']['response']['statusCode'])
#             return response
#
#         return wrapper
#
#     return decorate

