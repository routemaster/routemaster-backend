#!/usr/bin/python2
from __future__ import absolute_import, division
from datetime import date, datetime

from bson.json_util import dumps
from flask import abort, Flask, request
from pymongo import MongoClient, DESCENDING

DB_SERVER = 'localhost'
DB_NAME = 'routemaster'
DB_PORT = 27017
COLLECTIONS = ['popular_paths', 'routes', 'sessions', 'users', 'waypoints']

def collection(name):
    return MongoClient(DB_SERVER, DB_PORT)[DB_NAME][name]

def next_id(name):
    return collection('counters').findAndModify(query={'_id': name},
                                                update={'$inc': {'seq': 1}},
                                                new=True)['seq']

def paginate(page, number_per_page=25):
    return {'skip': (page - 1) * 25, 'limit': page * 25}

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/user/<int:uid>/', methods=['GET'])
def get_user(uid):
    user = collection('users').find_one({'uid': uid})
    if user:
        return dumps(user)
    else:
        abort(404)

@app.route('/user/<int:uid>/recent/<int:page>/', methods=['GET'])
def get_user_recent(uid, page):
    routes = collection('routes').find({'uid': uid},
                                       sort=[('date', DESCENDING)],
                                       **paginate(page))
    return dumps(routes)

@app.route('/user/<int:uid>/top/<int:page>/', methods=['GET'])
def get_user_top(uid, page):
    routes = collection('routes').find({'uid': uid},
                                       sort=[('efficiency', DESCENDING)],
                                       **paginate(page))
    return dumps(routes)

@app.route('/route/<int:rid>/', methods=['GET'])
def get_route(rid):
    route = collection('routes').find_one({'rid': rid})
    if route:
        return dumps(route)
    else:
        abort(404)

@app.route('/waypoint/<int:wid>/', methods=['GET'])
def get_waypoint(wid):
    waypoint = collection('waypoints').find_one({'wid': wid})
    if waypoint:
        return dumps(waypoint)
    else:
        abort(404)

@app.route('/waypoint/near/<coordinates>/', methods=['GET'])
def get_nearby_waypoints(coordinates):
    latitude, longitude = coordinates.split(',')
    # TODO: Query the database for nearby points
    return "This doesn't work yet."

@app.route('/popularpath/<int:wid>/', methods=['GET'])
def get_popularpath(wid):
    popularpath = collection('popularpaths').find_one({'wid': wid})
    if popularpath:
        return dumps(popularpath)
    else:
        abort(404)

@app.route('/popularpath/<int:pid>/top/<int:page>/', methods=['GET'])
def get_popularpath_top_routes(pid, page):
    routes = collection('routes').find({'pid': pid},
                                       sort=[('efficiency', DESCENDING)],
                                       **paginate(page))
    return dumps(routes)

@app.route('/leaders/efficiency/<int:page>/', methods=['GET'])
def get_top_efficiency(page):
    routes = collection('routes').find(sort=[('efficiency', DESCENDING)],
                                       **paginate(page))
    return dumps(routes)

@app.route('/leaders/exploration/<int:page>/', methods=['GET'])
def get_top_exploration(page):
    users = collection('users').find(sort=[('exploration', DESCENDING)],
                                     **paginate(page))
    return dumps(users)

@app.route('/user/', methods=['POST'])
def create_user():
    user = {'uid': next_id('users'),
            'name': request.form['name'],
            'registerDate': date.today(),
            'lastLoginTime': datetime.now(),
            'distance': 0,
            'exploration': 0}
    uid = collection('users').insert(user)
    return "Created user with id {}".format(uid)

@app.route('/route/', methods=['POST'])
def create_route():
    # Probably we should only do this with a valid session? How are we keeping
    # track of sessions? Cookies?
    route = {'rid': next_id('routes'),
             'uid': request.form['uid'],
             'pid': None,
             'date': request.form['date'],
             'start_wid': request.form['start_wid'],
             'end_wid': request.form['end_wid'],
             'disqualified': request.form['disqualified'],
             'distance': request.form['distance'],
             'efficiency': request.form['efficiency']}
    rid = collection('users').insert(user)
    return "Created route with id {}".format(rid)

@app.route('/waypoint/', methods=['POST'])
def create_waypoint():
    # Probably we should only do this with a valid session? How are we keeping
    # track of sessions? Cookies?
    waypoint = {'wid': next_id('waypoints'),
                'uid': request.form['uid'],
                'rid': request.form['rid'],
                'name': request.form['name'],
                'time': request.form['time'],
                'position': request.form['position'],
                'accuracy': request.form['accuracy']}
    wid = collection('waypoints').insert(waypoint)
    return "Created route with id {}".format(wid)

if __name__ == '__main__':
    # Set up counters
    #for name in COLLECTIONS:
    #    collection('counters').insert({'_id': name, 'seq': 0})
    app.run(host='0.0.0.0', port=8000, debug=True)
