package routemaster.jrm;

import routemaster.orm.*;
import com.mongodb.*;
import java.net.UnknownHostException;
import java.util.*;

public class DBFunctions {
        
    public DBFunctions() {
        //There doesn't seem to be anything here...
    }
    //
    public DBObject getUserFromDB(int uid) {
        BasicDBObject query = new BasicDBObject("uid", uid); //Query by user id
        DBCursor db = null;
        try{
            Orm o = new Orm();
            db = o.getUsersCollection().find(query);
        }
        catch(UnknownHostException e) {
            System.exit(1);
        }
        return db.next();
    }
    //
    public DBObject getRouteFromDB(int uid, Date stts, Date edts) {
        BasicDBObject query = new BasicDBObject("uid", uid)
            .append("stts", stts).append("edts", edts); //Query by uid, start time, end time
        DBCursor db = null;
        try{
            Orm o = new Orm();
            db = o.getUsersCollection().find(query);
        }
        catch(UnknownHostException e) {
            System.exit(1);
        }
        return db.next();
    }
    public ArrayList<Route> getAllUserRoutes(int uid) {
        BasicDBObject query = new BasicDBObject("uid", uid);
        DBCursor db = null;
        try{
            Orm o = new Orm();
            db = o.getUsersCollection().find(query);
        }
        catch(UnknownHostException e) {
            System.exit(1);
        }
        ArrayList<Route> r = new ArrayList<Route>();
        while(db.hasNext())
            r.add(new ParseJSON().parseRoute(db.next().toString()));
        return r;
    }
    //
    public DBObject getPPathsFromDB(double startlt, double startlg, double endlt, double endlg) {
        BasicDBObject query = new BasicDBObject("startlt", startlt)
            .append("startlg", startlg).append("endlg", endlg).append("endlt", endlt); //list of ppaths by lat/long
        DBCursor db = null;
        try{
            Orm o = new Orm();
            db = o.getUsersCollection().find(query);
        }
        catch(UnknownHostException e) {
            System.exit(1);
        }
        return db.next();
    }
    //
    public DBObject getWaypointFromDB(double lat, double lon, double alt) {
        BasicDBObject query = new BasicDBObject("lt", lat)
            .append("lg", lon).append("al", alt); //Use lat, long, alt to get wypt list
        DBCursor db = null;
        try{
            Orm o = new Orm();
            db = o.getUsersCollection().find(query);
        }
        catch(UnknownHostException e) {
            System.exit(1);
        }
        return db.next();
    }
    //
    public Waypoint[] getWaypointsFromRoute(int uid, Date stts, Date edts) {
        DBCursor cursor = getRouteFromDB(uid, stts, edts);
        Waypoint[] wypt = null;
        if(cursor.hasNext()) {
            Route r = new Route(cursor.next());
            //wypt = new Waypoint[r.getWypt().Length];
        }
        return wypt;  
    }
    //
    public DBObject getSessionFromDB(int uid) {
        BasicDBObject query = new BasicDBObject("uid", uid); //Query for session info w/ uid
        DBCursor db = null;
        try{
            Orm o = new Orm();
            db = o.getUsersCollection().find(query);
        }
        catch(UnknownHostException e) {
            System.exit(1);
        }
        return db.next();
    }
}
