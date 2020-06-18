import json


def decode_response(response):
    code = response.status_code
    data = {}
    try:
        data = json.loads(response.data.decode())
    except Exception as e:
        data = {'message': str(e)}
    return code, data
