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

# Add some routes
colin_r1 = Route(user_id=colin.id, date=date.today(), distance=11,
                 disqualified=False, efficiency=81, time=201)
colin_r2 = Route(user_id=colin.id, date=date.today(), distance=31,
                 disqualified=False, efficiency=91, time=2201)
colin_r3 = Route(user_id=colin.id, date=date.today(), distance=53,
                 disqualified=False, efficiency=31, time=9990201)
