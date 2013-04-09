import os
import tempfile
import unittest

from database import (PopularPath, Route, Session,
                      SQLAlchemySession, User, Waypoint)
import server

class RoutemasterTestCase(unittest.TestCase):
    def setUp(self):
        self.app = server.app.test_client()

    def test_hello_world(self):
        rv = self.app.get('/')
        assert 'Hello World!' in rv.data

if __name__ == '__main__':
    unittest.main()
