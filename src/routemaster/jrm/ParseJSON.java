package routemaster.jrm;

import java.util.Date;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import java.net.UnknownHostException;
import routemaster.orm.*;
import com.mongodb.*;
 
public class ParseJSON {

     //Keeping the getXFromDB separate. Currently not accounting for nonexistence in db
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
        User u = new User(new DBFunctions().getUserFromDB(uid));
        if(u.getUid() == uid)
            return u;
        try{
        u = new User(name, new Counter(new Orm().getUsersCollection(), name));
        return u;
        }
        catch(UnknownHostException e) {
            System.out.println(e);
        }
        return null;
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
        return new Session(new DBFunctions().getSessionFromDB(uid));
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
        return new Route(new DBFunctions().getRouteFromDB(uid, startTime, endTime));
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
        
        return new Waypoint(new DBFunctions().getWaypointFromDB(latitude, longitude, altitude));
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
        
        return new PopularPath(new DBFunctions().getPPathsFromDB(stlt, stlg, endlt, endlg));  
     }
}
