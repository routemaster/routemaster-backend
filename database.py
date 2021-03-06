from datetime import date, datetime
import os.path
from uuid import uuid4

from sqlalchemy import (Boolean, Column, create_engine, Date, DateTime,
                        Float, ForeignKey, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

DATABASE = 'routemaster.db'

# Define mapping classes for sqlalchemy
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    register_date = Column(Date, default=date.today)
    last_login_time = Column(DateTime, default=datetime.now)
    distance = Column(Integer, default=0)
    exploration = Column(Integer, default=0)
    routes = relationship('Route', backref='user')
    sessions = relationship('Session', backref='user')

class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    popularpath_id = Column(Integer, ForeignKey('popularpaths.id'),
                            nullable=True)
    date = Column(Date, default=date.today)
    distance = Column(Integer)
    disqualified = Column(Boolean, default=False)
    efficiency = Column(Integer)
    time = Column(Integer)
    start_name = Column(String)
    end_name = Column(String)
    waypoints = relationship('Waypoint', order_by='Waypoint.id',
                             backref='route')

class Waypoint(Base):
    __tablename__ = 'waypoints'
    id = Column(Integer, primary_key=True)
    route_id = Column(Integer, ForeignKey('routes.id'))
    accuracy = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)

class PopularPath(Base):
    __tablename__ = 'popularpaths'
    id = Column(Integer, primary_key=True)
    start_name = Column(String)
    end_name = Column(String)
    routes = relationship('Route', backref='popular_path')

class Session(Base):
    __tablename__ = 'sessions'
    uuid = Column(String, primary_key=True, default=uuid4)
    user_id = Column(Integer, ForeignKey('users.id'))
    time = Column(DateTime, default=datetime.now)

class Friendship(Base):
    __tablename__ = 'friendships'
    id = Column(Integer, primary_key=True)
    friender_id = Column(Integer, ForeignKey('users.id'))
    friendee_id = Column(Integer, ForeignKey('users.id'))

# Open the database using a RELATIVE path (an absolute path really does need
# four slashes there)
engine = create_engine('sqlite:///{}'.format(DATABASE))
SQLAlchemySession = sessionmaker(bind=engine)

# Initialize the database if it doesn't exist yet
if not os.path.exists(DATABASE):
    print "Creating sqlite database '{}'...".format(DATABASE)
    Base.metadata.create_all(engine)
    print "Done."
