#!/usr/bin/python2
from __future__ import absolute_import, division
from datetime import date, datetime

from flask import abort, Flask, request

from database import (PopularPath, Route, Session,
                      SQLAlchemySession, User, Waypoint)

# Initialize Flask
app = Flask(__name__)

@app.before_request
def before_request():
    g.db = SQLAlchemySession()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/user/<int:id>/', methods=['GET'])
def get_user(id):
    user = g.db.query(User).filter_by(id=id).first()
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
    route = g.db.query(Route).filter_by(id=rid).first()
    if route:
        return dumps(route)
    else:
        abort(404)

@app.route('/waypoint/<int:wid>/', methods=['GET'])
def get_waypoint(wid):
    waypoint = g.db.query(Waypoint).filter_by(id=wid).first()
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
def get_popularpath(pid):
    popularpath = g.db.query(PopularPath).filter_by(id=pid).first()
    if popularpath:
        return dumps(popularpath)
    else:
        abort(404)

@app.route('/popularpath/<int:pid>/top/<int:page>/', methods=['GET'])
def get_popularpath_top_routes(pid):
    routes = g.db.query(Route).filter_by(id=pid).first()
    if routes:
        return dumps(routes)
    else:
        abort(404)

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
    user = User(**request.form)
    g.db.add(user)
    g.db.commit()
    return "Created user with id {}".format(user.id)

@app.route('/route/', methods=['POST'])
def create_route():
    # Probably we should only do this with a valid session? How are we keeping
    # track of sessions? Cookies?
    route = Route(**request.form)
    g.db.add(route)
    g.db.commit()
    return "Created route with id {}".format(route.id)

@app.route('/waypoint/', methods=['POST'])
def create_waypoint():
    # Probably we should only do this with a valid session? How are we keeping
    # track of sessions? Cookies?
    waypoint = Waypoint(**request.form)
    g.db.add(waypoint)
    g.db.commit()
    return "Created waypoint with id {}".format(waypoint.id)

if __name__ == '__main__':
    # Set up counters
    #for name in COLLECTIONS:
    #    collection('counters').insert({'_id': name, 'seq': 0})
    app.run(host='0.0.0.0', port=8000, debug=True)
