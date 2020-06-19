from flask import Blueprint, current_app, jsonify, request
from uuid import uuid4, UUID
from project.util import response_failure, response_success

routes_blueprint = Blueprint('routes', __name__, template_folder='./templates')


@routes_blueprint.route('/j', methods=['GET'])
def j():
    return 'j success'


@routes_blueprint.route('/j/new_session', methods=['GET'])
def new_session():
    response = {'status': 'fail', 'message': 'Invalid payload.'}
    try:
        uuid = uuid4()
        current_app.controller.add_new_session(uuid)
        response = {'status': 'success', 'data': str(uuid)}
        return jsonify(response), 201

    except ValueError:
        return jsonify(response), 400
    except Exception:
        return jsonify(response), 400


@routes_blueprint.route('/j/repl', methods=['GET', 'POST'])
def repl():
    try:
        print(f'{request=}')
        print(request.get_json())
        uuid_str = request.get_json()['uuid']
        command = request.get_json()['command']
        uuid = UUID(uuid_str)
        if not current_app.controller.session_exists(uuid):
            return response_failure('invalid uuid', 403)
        else:
            result = current_app.controller.run_command(command, uuid)
            return response_success('success', 201, {'result': result})
    except ValueError:
        return response_failure('malformed uuid', 400)
    except KeyError:
        return response_failure('malformed request', 400)
    return response_failure('TODO', 666)
