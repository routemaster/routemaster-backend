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
   
    def test_put_route(self):
        walk = {'date': date.today(), 'distance': 100, 'disqualified': False, 'efficiency': 5, 'time': datetime.now()}
        r = requests.post(SERVER+'/route/', data=walk)
        assert r.status_code == 200
        testRoute = r.json()
        r2 = requests.get(SERVER+'/route/{}/'.format(testRoute['id']))
        dist = 100
        assert dist in r2.text

    def test_put_waypoint(self):
        point = {'name': 'newPoint', 'date': date.today(), 'accuracy': '4.3', 'latitude': '50.23', 'longitude': '23.45'}
        r = requests.post(SERVER+'/waypoint/', data=point)
        assert r.status_code == 200
        testPoint = r.json()
	r2 = requests.get(SERVER+'/waypoint/{}/'.format(testPoint['id']))
	acc = 4.3
	assert acc in r2.text

if __name__ == '__main__':
    results = unittest.main(exit=False).result
    if len(results.errors) == results.testsRun:
        print "Every single test failed. Good job."
        print "Did you forget to run the server before running the tests?"
