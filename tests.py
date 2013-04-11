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
        assert user['name'] == 'Colin Chan'
        r2 = requests.get(SERVER+'/user/{}/'.format(user['id']))
        assert r2.status_code == 200
        assert 'Colin Chan' in r2.text

    def test_put_route(self):
        route = {'date': date.today(), 'distance': 100, 'disqualified': False,
                'efficiency': 50, 'time': 305}
        r = requests.post(SERVER+'/route/', data=route)
        assert r.status_code == 200
        testRoute = r.json()
        assert testRoute['distance'] == 100
        assert testRoute['efficiency'] == 50
        r2 = requests.get(SERVER+'/route/{}/'.format(testRoute['id']))
        assert r2.status_code == 200
        assert '305' in r2.text

    def test_put_waypoint(self):
        point = {'name': 'newPoint', 'date': date.today(), 'accuracy': 43,
                 'latitude': 50.23, 'longitude': 23.45}
        r = requests.post(SERVER+'/waypoint/', data=point)
        assert r.status_code == 200
        testPoint = r.json()
        assert testPoint['name'] == 'newPoint'
        assert testPoint['latitude'] == 50.23
        r2 = requests.get(SERVER+'/waypoint/{}/'.format(testPoint['id']))
        assert r2.status_code == 200
        assert 4.3 in r2.text
        assert 'newPoint' in r2.text

if __name__ == '__main__':
    results = unittest.main(exit=False).result
    if len(results.errors) == results.testsRun:
        print "Every single test failed. Good job."
        print "Did you forget to run the server before running the tests?"
