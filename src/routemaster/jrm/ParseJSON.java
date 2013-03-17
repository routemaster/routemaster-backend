package routemaster.jrm;

import java.util.Date;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import routemaster.orm.*;
import com.mongodb.*;
 
public class ParseJSON {

     //Keeping the getXFromDB separate. Parse methods to elaborate on later
     public User parseUser(String s)
     {
        JSONParser parser = new JSONParser();
        //Set initial parse
        JSONObject userString = null;
        try {
            userString = (JSONObject) parser.parse(s);
        }
        catch(ParseException e) {
            System.exit(1);
        }
        //Get data
        String name = (String) userString.get("name");
        int uid = (Integer) userString.get("uid");
        Date registerDate = (Date) userString.get("regDate");
        Date lastLogin = (Date) userString.get("lastLogin");
        int rawExplo = (Integer) userString.get("rawExploration");
        //Do Something with the data
        
        return getUserFromDB(uid);        
     }
     public User getUserFromDB(int uid)
     {
         DBObject dbo = new DBFunctions().getUserFromDB(uid).next();
         return new User(dbo);
     }
     public Session parseSession(String s)
     {
        JSONParser parser = new JSONParser();
        //Set initial parse
        JSONObject sessionString = null;
        try {
            sessionString = (JSONObject) parser.parse(s);
        }
        catch(ParseException e) {
            System.exit(1);
        }
        //time-stamp currently is set on instantiation, so I assume no parse?
        Date timestamp = (Date) sessionString.get("timestamp");
        int uid = (Integer) sessionString.get("uid");
        long uuid = (Long) sessionString.get("uuid");
        //Do Something with the data
        
        return getSessionFromDB(uid);
     }
     public Session getSessionFromDB(int uid)
     {
         DBObject dbo = new DBFunctions().getSessionFromDB(uid).next();
         return new Session(dbo);
     }
     public Route parseRoute(String s)
     {
        JSONParser parser = new JSONParser();
        //Set initial parse
        JSONObject routeString = null;
        try {
            routeString = (JSONObject) parser.parse(s);
        }
        catch(ParseException e) {
            System.exit(1);
        }
        //
        JSONArray waypoints = (JSONArray) routeString.get("wypt");
        Date startTime = (Date) routeString.get("stts");
        Date endTime = (Date) routeString.get("edts");
        int uid = (Integer) routeString.get("uid");
        int efficiencyScore = (Integer) routeString.get("effs");
        boolean disqualified = (Boolean) routeString.get("disq");
        //Do Something with the data
        
        return getRouteFromDB(uid, startTime, endTime);
     }
     public Route getRouteFromDB(int uid, Date stts, Date edts)
     {
         DBObject dbo = new DBFunctions().getRouteFromDB(uid, stts, edts).next();
         return new Route(dbo);
     }
     public Waypoint parseWaypoint(String s)
     {
        JSONParser parser = new JSONParser();
    	//Set initial parse
    	JSONObject waypointString = null;
    	try {
    	    waypointString = (JSONObject) parser.parse(s);
    	}
    	catch(ParseException e) {
    	    System.exit(1);
    	}
        //
        Date timestamp = (Date) waypointString.get("ts");
        double latitude = (Double) waypointString.get("lt");
        double longitude = (Double) waypointString.get("lg");
        double altitude = (Double) waypointString.get("al");
        double accuracy = (Double) waypointString.get("ac");
        int uid = (Integer) waypointString.get("ui");
        //Do something with the data
        
        return getWyptFromDB(latitude, longitude, altitude);
     }
     public Waypoint getWyptFromDB(double lat, double lon, double alt) {
         DBObject dbo = new DBFunctions().getWaypointFromDB(lat, lon, alt).next();
         return new Waypoint(dbo);
     }
     public PopularPath parsePopularPaths(String s)
     {
         JSONParser parser = new JSONParser();
        //Set initial parse
         JSONObject popularString = null;
         try {
             popularString = (JSONObject) parser.parse(s);
         }
         catch(ParseException e) {
             System.exit(1);
         }
        //
        double stlt = (Double) popularString.get("startlt");
        double stlg = (Double) popularString.get("startlg");
        double endlt = (Double) popularString.get("endlt");
        double endlg = (Double) popularString.get("endlg");
        //Route r = popularString.get("route");
        //Do something with the data
        
        return getPPathsFromDB(stlt, stlg, endlt, endlg);
     }
     public PopularPath getPPathsFromDB(double startlat, double startlong, double endlat, double endlong) {
         DBObject dbo = new DBFunctions().getPPathsFromDB(startlat, startlong, endlat, endlong).next();
         return new PopularPath(dbo);
     }
}