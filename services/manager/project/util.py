from flask import jsonify


def response_failure(message, code, dict=None):
    response_object = {
        'status': 'fail',
        'message': message
    }
    if dict is not None:
        response_object.update(dict)
    return jsonify(response_object), code


def response_success(message, code, dict=None):
    response_object = {
        'status': 'success',
        'message': message
    }
    if dict is not None:
        response_object.update(dict)
    return jsonify(response_object), code
