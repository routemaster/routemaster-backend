#!/usr/bin/python2
from __future__ import absolute_import, division
from datetime import date, datetime
import json
import os.path

from flask import abort, Flask, g, make_response, redirect, request
from sqlalchemy import desc
from werkzeug import SharedDataMiddleware

from database import (Friendship, PopularPath, Route, Session,
                      SQLAlchemySession, User, Waypoint)

FRONTEND_BIN_DIR = '../frontend/bin'

def camel(s):
    return ''.join(b.upper() if a == '_' else b for a, b in zip(' '+s, s)
                   if b != '_')

def json_response(json):
    response = make_response(json)
    response.headers['content-type'] = 'application/json'
    return response

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
                value = value.isoformat()
            obj_dict[camel(column.name)] = value
        data.append(obj_dict)
    return json.dumps(data[0] if not_a_list else data, indent=2)

# Initialize Flask
app = Flask(__name__)

@app.before_request
def before_request():
    g.db = SQLAlchemySession()

@app.route('/')
def hello():
    return redirect('/index.html')

@app.route('/user/<int:id>/')
def get_user(id):
    user = g.db.query(User).filter_by(id=id).first()
    if user:
        return json_response(to_json(user))
    else:
        abort(404)

@app.route('/user/<int:uid>/recent/')
def get_user_recent_routes(uid):
    query = g.db.query(Route).filter_by(user_id=uid).order_by(desc(Route.id))
    return json_response(to_json(query.all()))

@app.route('/user/<int:uid>/top/')
def get_user_top_routes(uid):
    query = g.db.query(Route).filter_by(user_id=uid).order_by(
                desc(Route.efficiency))
    return json_response(to_json(query.all()))

@app.route('/user/<int:uid>/friends/')
def get_user_friends(uid):
    query = (g.db.query(Friendship, User).filter(Friendship.friendee_id==uid)
             .filter(Friendship.friender_id==User.id))
    friends = [user for friendship, user in query.all()]
    return json_response(to_json(friends))

@app.route('/user/<int:uid>/friend/<friendee_id>/', methods=['POST'])
def add_friendship(uid, friendee_id):
    # User <uid> does this in order to give user <friendee_id> access to
    # user <uid>'s data.
    friendship = Friendship(friender_id=uid, friendee_id=friendee_id)
    g.db.add(friendship)
    g.db.commit()
    return json_response(to_json(friendship))

@app.route('/route/<int:rid>/')
def get_route(rid):
    route = g.db.query(Route).filter_by(id=rid).first()
    if route:
        return json_response(to_json(route))
    else:
        abort(404)

@app.route('/route/<int:rid>/waypoints/')
def get_route_waypoints(rid):
    route = g.db.query(Route).filter_by(id=rid).first()
    if route:
        return json_response(to_json(route.waypoints))
    else:
        abort(404)

@app.route('/waypoint/<int:wid>/')
def get_waypoint(wid):
    waypoint = g.db.query(Waypoint).filter_by(id=wid).first()
    if waypoint:
        return json_response(to_json(waypoint))
    else:
        abort(404)

@app.route('/waypoint/near/<coordinates>/')
def get_nearby_waypoints(coordinates):
    latitude, longitude = map(float, coordinates.split(','))
    # Warning: The following code is not efficient. Avoid staring at it for
    # prolonged periods of time.
    routes = g.db.query(Route).all()
    named_waypoints = []
    for route in routes:
        start = route.waypoints[0]
        end = route.waypoints[-1]
        named_waypoints.append(((abs(start.latitude - latitude) +
                                 abs(start.longitude - longitude)),
                                route.start_name))
        named_waypoints.append(((abs(end.latitude - latitude) +
                                 abs(end.longitude - longitude)),
                                route.end_name))
    return json_response(json.dumps(min(sorted(named_waypoints))[1]))

@app.route('/popularpath/<int:wid>/')
def get_popularpath(pid):
    popularpath = g.db.query(PopularPath).filter_by(id=pid).first()
    if popularpath:
        return json_response(to_json(popularpath))
    else:
        abort(404)

@app.route('/popularpath/<int:pid>/top/')
def get_popularpath_top_routes(pid):
    query = (g.db.query(Route).filter_by(popularpath_id=pid)
                              .order_by(Route.efficiency))
    return json_response(to_json(query.all()))

@app.route('/leaders/efficiency/')
def get_top_routes_efficiency():
    query = g.db.query(Route).order_by(desc(Route.efficiency))
    return json_response(to_json(query.all()))

@app.route('/leaders/exploration/')
def get_top_routes_exploration():
    query = g.db.query(Route).order_by(Route.exploration)
    return json_response(to_json(query.all()))

@app.route('/userid/<username>/')
def get_user_id(username):
    user = g.db.query(User).filter_by(name=username).first()
    if user is None:
        user = User(name=username)
        g.db.add(user)
        g.db.commit()
    return json_response(json.dumps(user.id))

@app.route('/user/', methods=['POST'])
def create_user():
    user = User(name=request.json['name'])
    g.db.add(user)
    g.db.commit()
    return json_response(to_json(user))

@app.route('/route/', methods=['POST'])
def create_route():
    # Probably we should only do this with a valid session? How are we keeping
    # track of sessions? Cookies?
    f = request.json
    route = Route(user_id=f['userId'], distance=f['distance'],
                  disqualified=f['disqualified'],
                  efficiency=f['efficiency'], time=f['time'],
                  start_name=f['startName'], end_name=f['endName'])
    if 'popularpathId' in f:
        route.popularpath_id = f['popularpathId']
    g.db.add(route)
    g.db.commit()
    # Create waypoints
    for w in f['waypoints']:
        waypoint = Waypoint(route_id=route.id, accuracy=w['accuracy'],
                            latitude=w['latitude'], longitude=w['longitude'])
        g.db.add(waypoint)
    g.db.commit()
    return json_response(to_json(route))

if __name__ == '__main__':
    files_dir = os.path.join(os.path.dirname(__file__), FRONTEND_BIN_DIR)
    app.wsgi_app = SharedDataMiddleware(app.wsgi_app, { '/': files_dir},
                                        cache=False)
    app.run(host='0.0.0.0', port=8000, debug=True)
