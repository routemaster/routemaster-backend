package routemaster.jrm;

import routemaster.orm.*;
import org.json.simple.*;
import org.json.simple.parser.*;
import com.mongodb.*;
import java.util.ArrayList;
import java.util.Date;

public class UserFunctions {
    
    ParseJSON parser = new ParseJSON();
    
    public UserFunctions() {
        
    }
    //Void for now until functionality is developed
    public void CreateUser(JSONObject userinfo) {
        //Name
    }
    public ArrayList<Route> GetUserPaths(JSONObject userinfo) {
        //Uid
        User u = parser.parseUser(userinfo);
        ArrayList<Route> r = new DBFunctions().getAllUserRoutes(u.getUid()); //Array of routes
        return r;
        //Presumably the array list can be later translated back into JSON
    }
    public void UpdateLoginTime(JSONObject userinfo) {
        //Parameters are uid
        User u = parser.parseUser(userinfo);
        u.setLastLogin(new Date()); //Assuming it's run immediately
    }
    public void UpdateExploration(JSONObject userinfo) {
        //Parameters are uid, amt of increase
        User u = parser.parseUser(userinfo.toString());
        int expl = (Integer) userinfo.get("expl");        
        u.setRawExploration(u.getRawExploration() + expl);
    }
}
