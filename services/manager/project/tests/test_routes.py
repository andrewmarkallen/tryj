import unittest
import json
from uuid import UUID, uuid4

from project.tests.base import BaseTestCase
from project.tests.util import decode_response
from flask import current_app


class TestRoutes(BaseTestCase):
    """Tests for all routes"""

    def only_test_can_create_session(self):
        with self.client:
            code, data = decode_response(self.client.get('/j/new_session'))
            self.assertEqual(code, 201)
            uuid = UUID(data['data'])
            self.assertTrue(current_app.controller.session_exists(uuid))

    def post_repl(self, data):
        with self.client as client:
            response = client.post(
                '/j/repl',
                data=data,
                content_type='application/json'
            )
            return response

    def only_test_repl_needs_uuid(self):
        with self.client as client:
            data = json.dumps({'command': '3+3'})
            code, data = decode_response(client.post(
                '/j/repl',
                data=data,
                content_type='application/json'
                ))
            self.assertEqual(code, 400)
            self.assertEqual(data['message'], 'malformed request')

    def only_test_repl_needs_command(self):
        data = json.dumps({'uuid': str(uuid4())})
        code, data = decode_response(self.post_repl(data))
        self.assertEqual(code, 400)
        self.assertEqual(data['message'], 'malformed request')

    def only_test_repl_rejects_malformed_uuid(self):
        data = json.dumps({'uuid': 'bad_uuid', 'command': '3+3'})
        code, data = decode_response(self.post_repl(data))
        self.assertEqual(code, 400)
        self.assertEqual(data['message'], 'malformed uuid')

    def only_test_repl_rejects_invalid_uuid(self):
        data = json.dumps({'uuid': str(uuid4()), 'command': '3+3'})
        code, data = decode_response(self.post_repl(data))
        self.assertEqual(code, 403)
        self.assertEqual(data['message'], 'invalid uuid')

    def only_test_valid_repl_command_returns_response(self):
        _, data = decode_response(self.client.get('/j/new_session'))
        uuid = UUID(data['data'])
        data = json.dumps({'uuid': str(uuid), 'command': '3+3\n'})
        code, data = decode_response(self.post_repl(data))
        self.assertEqual(code, 201)
        self.assertEqual(data['result'], '6')
        data = json.dumps({'uuid': str(uuid), 'command': '+/i.10\n'})
        code, data = decode_response(self.post_repl(data))
        self.assertEqual(code, 201)
        self.assertEqual(data['result'], '45')

if __name__ == '__main__':
    unittest.main()
