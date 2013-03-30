package routemaster.jrm;

import routemaster.orm.*;
import org.json.simple.*;
import com.mongodb.*;

public class RouteFunctions {

    ParseJSON parser = new ParseJSON();
    
    public void CreateRoute(JSONObject userinfo) {
        //Uid
        User u = parser.parseUser(userinfo.toString());
        u.getUid();        
    }
    //
    public void GetEfficiencyScore(JSONObject routeinfo) {
        //Uid, route stts/edts
    }
    public void GetExplorationScore(JSONObject routeinfo) {
        //Uid, route stts/edts
    }
    public void EndRoute(JSONObject routeinfo) {
        //Parameters are date for final end time, uid, final expl score        
    }
    public void SetEfficiencyScore(JSONObject routeinfo) {
        //Uid, stts, new efficiency score
    }
    public void SetExplorationScore(JSONObject routeinfo) {
        //Uid, stts, new exploration score
    }
    public void DisqualifyRoute(JSONObject routeinfo) {
        //Uid, stts. /edts if disqualify only happens after path completion
    }
}
