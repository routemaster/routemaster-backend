package routemaster.jrm;

import java.util.Date;
import java.util.Iterator;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.JSONValue;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;
import routemaster.orm;
 
public class ParseJSON {

     public User parseUser(String s)
     {
        JSONParser parser = new JSONParser();
        //Set initial parse
        JSONObject userString = (JSONObject) parser.parse(s);
        //Get data
        String name = (String) userString.get("name");
        int uid = (int) userString.get("uid");
        Date registerDate = (Date) userString.get("regDate");
        Date lastLogin = (Date) userString.get("lastLogin");
        int rawExplo = (int) userString.get("rawExploration");
        //Do Something with the data
        return new User();
     }
     public Session parseSession(String s)
     {
        JSONParser parser = new JSONParser();
        //Set initial parse
        JSONObject sessionString = (JSONObject) parser.parse(s);
        //timestamp currently is set on instantiation, so I assume no parse?
        Date timestamp = (Date) sessionString.get("timestamp");
        int uid = (int) sessionString.get("uid");
        long uuid = (Long) sessionString.get("uuid");
        //Do Something with the data
        return new Session(uuid, uid);
     }
     public Route parseRoute(String s)
     {
        JSONParser parser = new JSONParser();
        //Set initial parse
        JSONObject routeString = (JSONObject) parser.parse(s);
        //
        JSONArray waypoints = (JSONArray) routeString.get("wypt");
        Date startTime = (Date) routeString.get("stts");
        Date endTime = (Date) routeString.get("edts");
        int uid = (int) routeString.get("uid");
        int efficiencyScore = (int) routeString.get("effs");
        boolean disqualified = (Boolean) routeString.get("disq");
        //Do Something with the data
        return new Route();
     }
     public Waypoint parseWaypoint(String s, Route r)
     {
        JSONParser parser = new JSONParser();
    	//Set initial parse
    	JSONObject waypointString = (JSONObject) parser.parse(s);
        //
        Date timestamp = (Date) waypointString.get("ts");
        double latitude = (Double) waypointString.get("lt");
        double longitude = (Double) waypointString.get("lg");
        double altitude = (Double) waypointString.get("al");
        double accuracy = (Double) waypointString.get("ac");
        int uid = (int) waypointString.get("ui");
        //Do something with the data
        return new Waypoint();
     }
     public PopularPath parsePopularPaths(String s)
     {
         JSONParser parser = new JSONParser();
        //Set initial parse
         JSONObject popularString = (JSONObject) parser.parse(s);
        //
        JSONArray start = (JSONArray) popularString.get("start");
        double[] st = {(Double)start.get(0), (Double)start.get(1), (Double)start.get(2)};
        JSONArray end = (JSONArray) popularString.get("end");
        double[] ed = {(Double)end.get(0), (Double)end.get(1), (Double)end.get(2)};
        Route popRoute = parseRoute(popularString.get("route"));
        //Do something with the data
        return new PopularPath();
     }
}