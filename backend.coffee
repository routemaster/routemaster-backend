express = require "express"
mongodb = require "mongodb"
_ = require "underscore"

# Feel free to adjust these
config =
    app:
        port: 8081
    db:
        server: "localhost"
        name: "routemaster"
        port: 27017

# Launch server
app = express()
app.use express.compress()
app.use express.bodyParser()

# Error handling
app.use (err, req, resp, next) ->
    resp.json 500, error: "Internal server error"

# Logging
app.use (err, req, resp, next) ->
    console.log "#{req.method}: #{req.url}"
    next()

# Connect to MongoDB. Once connected, fill in the routing rules
new mongodb.MongoClient(
    new mongodb.Server config.db.server, config.db.port, native_parser: true
).open (err, connection) ->
    if err?
        return console.error "MongoDB Connection Error: #{err}"

    # Intialize database and collections
    db = connection.db config.db.name
    c =
        counters: db.collection "counters"
        users: db.collection "users"
        routes: db.collection "routes"

    # Generic helper functions
    nextId = (name, callback, safe=true) ->
        counters.findAndModify(
            {_id: name}, {$inc: {seq: 1}}, {new: true, journal: safe},
            (err, doc) -> callback err, doc[name]
        )

    # URL handlers (should be pretty simple)
    # Default Handler
    app.get "/", (req, resp) ->
        resp.end "Hello, World!\n" # It's the end of the world!

    # Create User
    app.post "/user/", (req, resp) -> nextId "users", (err, uid) ->
        if err? or not _.isString(req.body.name)
            return resp.json "Bad username"
        user =
            uid: uid
            name: req.params.name
            registerDate: Date.now()
            lastLogin: null
            rawExploration: 0
        c.users.insert user, {journal: true}, (err) ->
            if err?
                return resp.json 500, "User registration failed"
            resp.json 200, result: "success"

    # Read User
    app.get "/user/:uid/", (req, resp) ->
        c.users.find_one {uid: req.params.uid}, resp.json

    # Update User
    app.put "/user/:uid/", (req, resp) ->
        updates = {}
        for key in ["name", "lastLogin"]
            updates[key] = resp.body[key]
        c.users.update {uid: uid}, {$set: updates}, (err) ->
            if err?
                resp.json 500, error: "User update failed"
            else
                resp.json 201, result: "success"

    # Delete User
    app.delete "/user/:uid/", (req, resp) ->
        c.users.remove {uid: req.params.uid}, {}, (err) ->
            if err?
                resp.json 500, error: "User deletion failed"
            else
                resp.json 410, result: "success"

    app.listen config.app.port
    console.log "Server is running: http://localhost:#{config.app.port}"
