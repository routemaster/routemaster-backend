#!/usr/bin/python2
from __future__ import absolute_import, division
from datetime import date, datetime
import json
import os.path
from time import mktime

from dateutil.parser import parse as parse_date
from flask import abort, Flask, g, request

from database import (Friendship, PopularPath, Route, Session,
                      SQLAlchemySession, User, Waypoint)

def to_json(objects):
    not_a_list = False
    if not isinstance(objects, list):
        not_a_list = True
        objects = [objects]
    data = []
    for obj in objects:
        obj_dict = {}
        for column in obj.__table__.columns:
            value = getattr(obj, column.name)
            if isinstance(value, (date, datetime)):
                value = mktime(value.timetuple())
            obj_dict[column.name] = value
        data.append(obj_dict)
    return json.dumps(data[0] if not_a_list else data)

# Initialize Flask
app = Flask(__name__)

@app.before_request
def before_request():
    g.db = SQLAlchemySession()

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/user/<int:id>/')
def get_user(id):
    user = g.db.query(User).filter_by(id=id).first()
    if user:
        return to_json(user)
    else:
        abort(404)

@app.route('/user/<int:uid>/recent/')
def get_user_recent_routes(uid):
    query = g.db.query(Route).filter_by(user_id=uid).order_by(Route.date)
    return to_json(query.all())

@app.route('/user/<int:uid>/top/')
def get_user_top_routes(uid):
    query = g.db.query(Route).filter_by(user_id=uid).order_by(Route.efficiency)
    return to_json(query.all())

@app.route('/user/<int:uid>/friends/')
def get_user_friends(uid):
    query = (g.db.query(Friendship, User).filter(Friendship.friendee_id==uid)
             .filter(Friendship.friender_id==User.id))
    friends = [user for friendship, user in query.all()]
    return to_json(friends)

@app.route('/user/<int:uid>/friend/<friendee_id>/', methods=['POST'])
def add_friendship(uid, friendee_id):
    # User <uid> does this in order to give user <friendee_id> access to
    # user <uid>'s data.
    friendship = Friendship(friender_id=uid, friendee_id=friendee_id)
    g.db.add(friendship)
    g.db.commit()
    return to_json(friendship)

@app.route('/route/<int:rid>/')
def get_route(rid):
    route = g.db.query(Route).filter_by(id=rid).first()
    if route:
        return to_json(route)
    else:
        abort(404)

@app.route('/route/<int:rid>/waypoints/')
def get_route_waypoints(rid):
    route = g.db.query(Route).filter_by(id=rid).first()
    if route:
        return to_json(route.waypoints)
    else:
        abort(404)

@app.route('/waypoint/<int:wid>/')
def get_waypoint(wid):
    waypoint = g.db.query(Waypoint).filter_by(id=wid).first()
    if waypoint:
        return to_json(waypoint)
    else:
        abort(404)

@app.route('/waypoint/near/<coordinates>/')
def get_nearby_waypoints(coordinates):
    latitude, longitude = coordinates.split(',')
    # TODO: Query the database for nearby points
    return "This doesn't work yet."

@app.route('/popularpath/<int:wid>/')
def get_popularpath(pid):
    popularpath = g.db.query(PopularPath).filter_by(id=pid).first()
    if popularpath:
        return to_json(popularpath)
    else:
        abort(404)

@app.route('/popularpath/<int:pid>/top/')
def get_popularpath_top_routes(pid):
    query = (g.db.query(Route).filter_by(popularpath_id=pid)
                              .order_by(Route.efficiency))
    return to_json(query.all())

@app.route('/leaders/efficiency/')
def get_top_routes_efficiency():
    query = g.db.query(Route).order_by(Route.efficiency)
    return to_json(query.all())

@app.route('/leaders/exploration/')
def get_top_routes_exploration():
    query = g.db.query(Route).order_by(Route.exploration)
    return to_json(query.all())

@app.route('/user/', methods=['POST'])
def create_user():
    user = User(name=request.json['name'])
    g.db.add(user)
    g.db.commit()
    return to_json(user)

@app.route('/route/', methods=['POST'])
def create_route():
    # Probably we should only do this with a valid session? How are we keeping
    # track of sessions? Cookies?
    f = request.json
    route = Route(user_id=f['user_id'], distance=f['distance'],
                  disqualified=f['disqualified'],
                  efficiency=f['efficiency'], time=f['time'],
                  start_name=f['start_name'], end_name=f['end_name'])
    if 'popularpath_id' in f:
        route.popularpath_id = f['popularpath_id']
    g.db.add(route)
    g.db.commit()
    # Create waypoints
    for w in f['waypoints']:
        waypoint = Waypoint(route_id=route.id, accuracy=w['accuracy'],
                            latitude=w['latitude'], longitude=w['longitude'])
        g.db.add(waypoint)
    g.db.commit()
    return to_json(route)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
