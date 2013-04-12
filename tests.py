from datetime import date, datetime
import unittest

import requests

SERVER = 'http://localhost:8000'

class RoutemasterTestCase(unittest.TestCase):

    def test_hello_world(self):
        r = requests.get(SERVER+'/')
        assert r.text == 'Hello World!'

    def test_add_user(self):
        # We're going to add a user to the database!
        colin = {'name': 'Colin Chan'}
        # Send the request to the server and save the response
        r = requests.post(SERVER+'/user/', data=colin)
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
        colin = {'name': 'Colin Chan'}
        colin_id = requests.post(SERVER+'/user/', data=colin).json()['id']
        # Add a route
        route = {'user_id': colin_id, 'date': date.today().isoformat(),
                 'distance': 100, 'disqualified': 0, 'efficiency': 50,
                 'time': 305}
        r = requests.post(SERVER+'/route/', data=route)
        assert r.status_code == 200
        # Do some spot checks to make sure the server returns the right stuff
        route = r.json()
        assert route['distance'] == 100
        assert route['efficiency'] == 50
        r = requests.get(SERVER+'/route/{}/'.format(route['id']))
        assert r.status_code == 200
        assert '305' in r.text
        # Next, add a waypoint
        point = {'name': 'newPoint', 'date': date.today().isoformat(),
                 'accuracy': 43, 'latitude': 50.23, 'longitude': 23.45,
                 'user_id': colin_id, 'route_id': route['id']}
        r = requests.post(SERVER+'/waypoint/', data=point)
        assert r.status_code == 200
        # More spot checks
        point = r.json()
        assert point['name'] == 'newPoint'
        assert point['latitude'] == 50.23
        r = requests.get(SERVER+'/waypoint/{}/'.format(point['id']))
        assert r.status_code == 200
        assert '43' in r.text
        assert 'newPoint' in r.text

    def test_add_friendship(self):
        # Add some users
        colin = {'name': 'Colin Chan'}
        ben = {'name': 'Benjamin Woodruff'}
        colin_id = requests.post(SERVER+'/user/', data=colin).json()['id']
        ben_id = requests.post(SERVER+'/user/', data=ben).json()['id']
        # Colin adds Ben as a friend!
        r = requests.post(SERVER+'/user/{}/friend/{}/'.format(colin_id,
                                                              ben_id))
        assert r.status_code == 200
        friendship = r.json()
        assert friendship['friender_id'] == colin_id
        assert friendship['friendee_id'] == ben_id

if __name__ == '__main__':
    results = unittest.main(exit=False).result
    if len(results.errors) == results.testsRun:
        print "Every single test failed. Good job."
        print "Did you forget to run the server before running the tests?"
