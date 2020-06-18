import unittest
from project.controller import Controller
from project.session import Session
from project.tests.base import BaseTestCase
from uuid import uuid4
from flask import current_app


class TestController(BaseTestCase):
    """Test the Controller class (which handles creating docker sessions)"""

    def test_can_add_to_session_queue(self):
        controller = current_app.controller
        uuid = uuid4()
        controller.add_new_session(uuid)
        self.assertTrue(controller.session_exists(uuid))

    def test_can_not_re_add_existing_session(self):
        controller = current_app.controller
        uuid = uuid4()
        controller.add_new_session(uuid)
        self.assertFalse(controller.add_new_session(uuid))


if __name__ == '__main__':
    unittest.main()
