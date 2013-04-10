from datetime import date, datetime
import unittest

import requests

SERVER = 'http://localhost:8000'

class RoutemasterTestCase(unittest.TestCase):

    def test_hello_world(self):
        r = requests.get(SERVER+'/')
        assert r.text == 'Hello World!'

    def test_put_user(self):
        colin = {'name': 'Colin Chan', 'register_date': date.today()}
        r = requests.post(SERVER+'/user/', data=colin)
        assert r.status_code == 200
        user = r.json()
        r2 = requests.get(SERVER+'/user/{}/'.format(user['id']))
        assert 'Colin Chan' in r2.text

if __name__ == '__main__':
    results = unittest.main(exit=False).result
    if len(results.errors) == results.testsRun:
        print "Every single test failed. Good job."
        print "Did you forget to run the server before running the tests?"
