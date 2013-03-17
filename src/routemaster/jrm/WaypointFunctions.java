package routemaster.jrm;

import routemaster.orm.*;
import org.json.simple.*;
import com.mongodb.*;

public class WaypointFunctions {
    
    public void CreateWaypoint(JSONObject info) {
        //Uid, wypt ts/lat/long/alt, route stts/edts
        Waypoint w = new ParseJSON().parseWaypoint(info.toString());
        Route r = new ParseJSON().parseRoute(info.toString());
        r.addWypt(w);
    }
}
