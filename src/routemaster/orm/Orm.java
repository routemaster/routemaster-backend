package routemaster.orm;

import com.mongodb.MongoClient;
import com.mongodb.DB;

public class Orm {
    private MongoClient connection = new MongoClient();
    private DB database = connection.getDB("routemaster");

    public Orm() {
        
    }

    public DBCollection getUsersCollection() {
        return database.getCollection("users");
    }

    public DBCollection getCountersCollection() {
        return database.getCollection("counters");
    }

    public DBCollection getSessionsCollection() {
        return database.getCollection("sessions");
    }

    public DBCollection getRoutesCollection() {
        return database.getCollection("routes");
    }
    
    public DBCollection getWaypointsCollection() {
        return database.getCollection("waypoints");
    }

    public DBCollection getPopularPathsCollection() {
        return database.getCollection("popularPaths");
    }
}
