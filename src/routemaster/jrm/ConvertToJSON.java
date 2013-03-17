package routemaster.jrm;

import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import routemaster.orm.*;

public class ConvertToJSON {
    
    public JSONOBject convertUser(User u)
    {
        JSONObject userJSON = new JSONObject();
        userJSON.put("name", u.getName());
        userJSON.put("uid", u.getUid());
        userJSON.put("regDate", u.getRegisterDate());
        userJSON.put("lastLogin", u.getLastLogin());
        userJSON.put("rawExploration", u.getRawExploration());
    
        return userJSON;
    }
    public JSONObject convertSession(Session s)
    {
        JSONObject sessionJSON = new JSONObject();
        sessionJSON.put("uuid", s.getUuid());
        sessionJSON.put("uid", s.getUid());
        sessionJSON.put("timestamp", s.getTimestamp());
    	
        return sessionJSON;
    }
    public JSONObject convertRoute(Route r)
    {
        JSONObject routeJSON = new JSONObject();
        routeJSON.put("stts", r.getStts());
        routeJSON.put("edts", r.getEdts());
        routeJSON.put("uid", r.getUid());
        routeJSON.put("effs", r.getEffs());
        routeJSON.put("disq", r.getDisq());
    
        Waypoint[] wypts = r.getWypt();
        JSONArray waypoints = new JSONArray();
        //Waypoint array
        for(int i = 0; i < wypts.length; i++)
            waypoints.add(convertWaypoint(wypts[i]));
        routeJSON.put("wypt", waypoints);
        
        return routeJSON;
    }
    public JSONObject convertWaypoint(Waypoint wypt)
    {
        JSONObject waypointJSON = new JSONObject();
    	waypointJSON.put("ts", wypt.getTs());
        waypointJSON.put("lt", wypt.getLt());
        waypointJSON.put("lg", wypt.getLg());
        waypointJSON.put("at", wypt.getAl());
        waypointJSON.put("ac", wypt.getAc());
        waypointJSON.put("ui", wypt.getUi());
        
        return waypointJSON;
    }
    public JSONObject convertPopularPath(PopularPath p)
    {
        JSONObject popJSON = new JSONObject();
        JSONArray start = new JSONArray();
        for(int i = 0; i < p.getStart().length; i++)
            start.add(p.getStart()[i]);
        JSONArray end = new JSONArray();
        for(int j = 0; j < p.getEnd().length; j++)
            end.add(p.getEnd()[i]);
    	popJSON.put("start", start);
    	popJSON.put("end", end);
    	popJSON.put("route", convertRoute(p.getRoute()));
       
        return popJSON;
    }
}