from flask import Blueprint

routes_blueprint = Blueprint('routes', __name__, template_folder='./templates')


@routes_blueprint.route('/j', methods=['GET'])
def j():
    return 'j success'
