package routemaster.jrm;

import routemaster.orm.*;

import com.mongodb.*;

public class DBFunctions {
        
    public DBFunctions() {
        //Blah
    }
    public DBCursor getUserFromDB(int uid) {
        BasicDBObject query = new BasicDBObject("uid", uid);
        try{
            Orm o = new Orm();
        }
        catch(UnknownHostException e)
            System.exit(1);
        DBCursor db = o.getUsersCollection().find(query);
        return db;
    }
    public DBCursor getRouteFromDB(int uid, int stts, int edts) {
        BasicDBObject query = new BasicDBObject("uid", uid).append("stts", stts).append("edts", edts);
        try{
            Orm o = new Orm();
        }
        catch(UnknownHostException e)
            System.exit(1);
        DBCursor db = o.getRoutesCollection().find(query);
        return db;
        //return new Route(db);
    }
    public DBCursor getPPathsFromDB(double startlt, double startlg, double endlt, double endlg) {
        BasicDBObject query = new BasicDBObject("startlt", startlt)
            .append("startlg", startlg).append("endlg", endlg).append("endlt", endlt);
        
        try{
            Orm o = new Orm();
        }
        catch(UnknownHostException e)
            System.exit(1);
        DBCursor db = o.getPopularPathsCollection().find(query);
        return db;
        //return new PopularPath(db);
    }
    public DBCursor getWaypointFromDB(double lat, double lon, double alt) {
        BasicDBObject query = new BasicDBObject("lt", lat).append("lg", lg).append("al", alt);
        try{
            Orm o = new Orm();
        }
        catch(UnknownHostException e)
            System.exit(1);
        DBCursor db = o.getWaypointsCollection().find(query);
        return db;
        //return new Waypoint(db);
    }
}
