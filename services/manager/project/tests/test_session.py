import unittest
from project.session import Session
from project.tests.base import BaseTestCase
from uuid import uuid4


class TestSession(BaseTestCase):
    """Test the Session class (which handles sessions)"""

    def test_can_create_session_object_and_resources(self):
        uuid = uuid4()
        session = Session(uuid)
        self.assertEqual(session.id, uuid)

    def test_session_can_execute_code(self):
        uuid = uuid4()
        session = Session(uuid)
        result = session.write("9!:14 ''\n")
        self.assertIn('j901/j64/linux/', result)

    def test_multiple_sessions_dont_block_eachother(self):
        self.fail("todo")


if __name__ == '__main__':
    unittest.main()
