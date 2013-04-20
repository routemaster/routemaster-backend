from datetime import date, datetime

from database import (Friendship, PopularPath, Route, Session,
                      SQLAlchemySession, User, Waypoint)

db = SQLAlchemySession()

# Add some users
colin = User(name='Colin Chan')
ben = User(name='Benjamin Woodruff')
ron = User(name='Ron Paul')
mitt = User(name='Mitt Romney')
al = User(name='Al Gore')
john = User(name='John McCain')
db.add_all([colin, ben, ron, mitt, al, john])
db.commit()

# Add some friendships
colin_ben = Friendship(friender_id=colin.id, friendee_id=ben.id)
colin_ron = Friendship(friender_id=colin.id, friendee_id=ron.id)
colin_mitt = Friendship(friender_id=colin.id, friendee_id=mitt.id)
colin_al = Friendship(friender_id=colin.id, friendee_id=al.id)
colin_john = Friendship(friender_id=colin.id, friendee_id=john.id)
ben_colin = Friendship(friender_id=ben.id, friendee_id=colin.id)
ron_colin = Friendship(friender_id=ron.id, friendee_id=colin.id)
al_colin = Friendship(friender_id=al.id, friendee_id=colin.id)
db.add_all([colin_ben, colin_ron, colin_mitt, colin_al, colin_john, ben_colin,
            ron_colin, al_colin])
db.commit()

# Add some routes
colin_r1 = Route(user_id=colin.id, distance=11, efficiency=81, time=201,
                 start_name='CISE', end_name='Reitz')
colin_r2 = Route(user_id=colin.id, distance=31, efficiency=91, time=2201,
                 start_name='CISE', end_name='Library West')
colin_r3 = Route(user_id=colin.id, distance=553, efficiency=31, time=10201,
                 start_name='CISE', end_name='Little Hall')
db.add_all([colin_r1, colin_r2, colin_r3])
db.commit()

# Add some waypoints
# CISE -> Reitz
w1 = Waypoint(route_id=colin_r1.id, accuracy=20,
              latitude=29.648158, longitude=-82.344515)
w2 = Waypoint(route_id=colin_r1.id, accuracy=20,
              latitude=29.647691, longitude=-82.344617)
w3 = Waypoint(route_id=colin_r1.id, accuracy=20,
              latitude=29.647939, longitude=-82.345347)
w4 = Waypoint(route_id=colin_r1.id, accuracy=20,
              latitude=29.64723, longitude=-82.345502)
w5 = Waypoint(route_id=colin_r1.id, accuracy=20,
              latitude=29.646745, longitude=-82.346334)
w6 = Waypoint(route_id=colin_r1.id, accuracy=20,
              latitude=29.646582, longitude=-82.346977)
w7 = Waypoint(route_id=colin_r1.id, accuracy=20,
              latitude=29.646414, longitude=-82.347508)
db.add_all([w1, w2, w3, w4, w5, w6, w7])
# CISE -> Library West
w8 = Waypoint(route_id=colin_r2.id, accuracy=33,
              latitude=29.64823, longitude=-82.34439)
w9 = Waypoint(route_id=colin_r2.id, accuracy=12,
              latitude=29.64904, longitude=-82.34364)
w10 = Waypoint(route_id=colin_r2.id, accuracy=5,
              latitude=29.65035, longitude=-82.34293)
w11 = Waypoint(route_id=colin_r2.id,  accuracy=21,
              latitude=29.65111, longitude=-82.34285)
db.add_all([w8, w9, w10, w11])
# CISE -> Little Hall
w12 = Waypoint(route_id=colin_r3.id, accuracy=17,
              latitude=29.64823, longitude=-82.34439)
w13 = Waypoint(route_id=colin_r3.id, accuracy=30,
              latitude=29.64858, longitude=-82.3433)
w14 = Waypoint(route_id=colin_r3.id, accuracy=23,
               latitude=29.64854, longitude=-82.34206)
w15 = Waypoint(route_id=colin_r3.id, accuracy=11,
               latitude=29.64875, longitude=-82.34102)
db.add_all([w12, w13, w14, w15])
db.commit()

db.close()
