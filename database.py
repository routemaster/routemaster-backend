from datetime import date, datetime
from uuid import uuid4

from sqlalchemy import (Boolean, Column, create_engine, Date, DateTime,
                        Float, ForeignKey, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

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
    popularpath_id = Column(Integer, ForeignKey('popularpaths.id'))
    date = Column(Date)
    start_id = Column(Integer, ForeignKey('waypoints.id'))
    end_id = Column(Integer, ForeignKey('waypoints.id'))
    distance = Column(Integer)
    disqualified = Column(Boolean)
    efficiency = Column(Integer)
    time = Column(Integer)

class Waypoint(Base):
    __tablename__ = 'waypoints'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    route_id = Column(Integer, ForeignKey('routes.id'))
    name = Column(String)
    date = Column(Date)
    accuracy = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    route = relationship('Route', backref='waypoints', foreign_keys=[route_id])

class PopularPath(Base):
    __tablename__ = 'popularpaths'
    id = Column(Integer, primary_key=True)
    start_id = Column(Integer, ForeignKey('waypoints.id'))
    end_id = Column(Integer, ForeignKey('waypoints.id'))
    routes = relationship('Route', backref='popular_path')

class Session(Base):
    __tablename__ = 'sessions'
    uuid = Column(String, primary_key=True, default=uuid4)
    user_id = Column(Integer, ForeignKey('users.id'))
    time = Column(DateTime, default=datetime.now)

# Open the database using a RELATIVE path (an absolute path really does need
# four slashes there)
engine = create_engine('sqlite:///routemaster.db')
SQLAlchemySession = sessionmaker(bind=engine)
