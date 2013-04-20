from datetime import date, datetime
from json import dumps
import unittest

import requests

SERVER = 'http://localhost:8000'
JSON_HEADER = {'content-type': 'application/json'}

class RoutemasterTestCase(unittest.TestCase):

    def test_add_user(self):
        # We're going to add a user to the database!
        colin = dumps({'name': 'Colin Chan'})
        # Send the request to the server and save the response
        r = requests.post(SERVER+'/user/', data=colin, headers=JSON_HEADER)
        # Check that we get the correct status code (200 means Success)
        assert r.status_code == 200
        # Convert the response json into a dictionary
        user = r.json()
        # Make sure this conversion worked and has the right data
        assert user['name'] == 'Colin Chan'
        # Request our new user by id from the server
        r2 = requests.get(SERVER+'/user/{}/'.format(user['id']))
        # Check that the request was successful and has the right data
        assert r2.status_code == 200
        assert 'Colin Chan' in r2.text

    def test_add_route_and_waypoints(self):
        # We need a valid user id to add a route
        colin = dumps({'name': 'Colin Chan'})
        r = requests.post(SERVER+'/user/', data=colin, headers=JSON_HEADER)
        colin_id = r.json()['id']
        # Add a route
        waypoints = [{'accuracy': 43, 'latitude': 50.23, 'longitude': 23.45},
                     {'accuracy': 40, 'latitude': 60.23, 'longitude': 23.45},
                     {'accuracy': 41, 'latitude': 70.23, 'longitude': 23.45}]
        route = dumps({'userId': colin_id, 'date': date.today().isoformat(),
                       'distance': 100, 'disqualified': 0, 'efficiency': 50,
                       'time': 305, 'startName': 'Epcot',
                       'endName': 'the beach', 'waypoints': waypoints})
        r = requests.post(SERVER+'/route/', data=route, headers=JSON_HEADER)
        assert r.status_code == 200
        # Do some spot checks to make sure the server returns the right stuff
        route = r.json()
        assert route['distance'] == 100
        assert route['efficiency'] == 50
        r = requests.get(SERVER+'/route/{}/'.format(route['id']))
        assert r.status_code == 200
        assert '305' in r.text
        r = requests.get(SERVER+'/route/{}/waypoints/'.format(route['id']))
        assert '50.23' in r.text
        assert '60.23' in r.text
        waypoints = r.json()
        assert len(waypoints) == 3

    def test_add_friendship(self):
        # Add some users
        colin = dumps({'name': 'Colin Chan'})
        ben = dumps({'name': 'Benjamin Woodruff'})
        r = requests.post(SERVER+'/user/', data=colin, headers=JSON_HEADER)
        colin_id = r.json()['id']
        r = requests.post(SERVER+'/user/', data=ben, headers=JSON_HEADER)
        ben_id = r.json()['id']
        # Colin adds Ben as a friend!
        r = requests.post(SERVER+'/user/{}/friend/{}/'.format(colin_id,
                                                              ben_id))
        assert r.status_code == 200
        friendship = r.json()
        assert friendship['frienderId'] == colin_id
        assert friendship['friendeeId'] == ben_id

if __name__ == '__main__':
    results = unittest.main(exit=False).result
    if len(results.errors) == results.testsRun:
        print "Every single test failed. Good job."
        print "Did you forget to run the server before running the tests?"
