#!/usr/bin/python2
from __future__ import absolute_import, division
from datetime import date, datetime

from flask import abort, Flask, request
from sqlalchemy import (Boolean, Column, create_engine, Date, DateTime,
                        Float, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Define mapping classes for sqlalchemy
Base = declarative_base()

User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    register_date = Column(Date)
    last_login_time = Column(DateTime)
    distance = Column(Integer)
    exploration = Column(Integer)
    routes = relationship('Route', backref='user')
    sessions = relationship('Session', backref='user')

Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    popularpath_id = Column(Integer, ForeignKey('popularpaths.id'))
    date = Column(Date)
    start_id = Column(Integer, ForeignKey('waypoints.id'))
    end_id = Column(Integer, ForeignKey('waypoints.id'))
    distance = Column(Integer)
    disqualified = Column(Boolean)
    efficiency = Column(Integer)
    time = Column(Integer)
    waypoints = relationship('Waypoint', backref='route')

Waypoint(Base):
    __tablename__ = 'waypoints'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    route_id = Column(Integer, ForeignKey('routes.id'))
    name = Column(String)
    date = Column(Date)
    accuracy = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)

PopularPath(Base):
    __tablename__ = 'popularpaths'
    id = Column(Integer, primary_key=True)
    start_id = Column(Integer, ForeignKey('waypoints.id'))
    end_id = Column(Integer, ForeignKey('waypoints.id'))
    routes = relationship('Route', backref='popular_path')

Session(Base):
    __tablename__ = 'sessions'
    uuid = Column(String, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    time = Column(DateTime)

def paginate(page, number_per_page=25):
    return {'skip': (page - 1) * 25, 'limit': page * 25}

# Open the database using a RELATIVE path (an absolute path really does need
# four slashes there)
engine = create_engine('sqlite:///routemaster.db')
Session = sessionmaker(bind=engine)

# Initialize Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/user/<int:id>/', methods=['GET'])
def get_user(id):
    session = Session()
    user = session.query(User).filter_by(id=id).first()
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
