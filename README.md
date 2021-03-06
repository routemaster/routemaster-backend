Routemaster (Backend)
=====================

![Logo](https://www.cise.ufl.edu/~woodruff/routemaster/logo_small.png)

Walking is boring. Let's turn it into an online multiplayer competitive game!

- Map your walking, running, biking, or even driving paths with GPS on your
  phone.
- View past routes, and the routes of your friends
- Earn points for walking efficient routes
- Earn points for exploring more area than your friends

Repository Organization
-----------------------

This is the repository for our back-end. It should store routes, user data, and
other associated information in a MongoDB database, and serve it to the
front-end as needed via a JSON-based API. With a few exceptions, the code in
this repository should be written in Python!!!.

Building the Project
--------------------

This isn't going to work well on Windows...

1. Install Python 2.7 and virtualenv

2. Clone the repository

    $ git clone https://github.com/routemaster/routemaster-backend.git

3. Initialize the repository directory with virtualenv

    $ virtualenv routemaster-backend

4. Install the needed packages

    $ cd routemaster-backend/
    $ bin/pip install -r requirements.txt

3. Run the server

    $ bin/python server.py

4. With the server running, you can run the tests

    $ bin/python tests.py

Project Scope
-------------

This project is being created by a team of eight students at the University of
Florida for CEN3031, Introduction to Software Engineering. It will be developed
in three Scrum sprints over the course of the Spring 2013 semester.

License
-------

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along
with this program. If not, see <http://www.gnu.org/licenses/>.
