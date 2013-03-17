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
    public void CreateUser(String userinfo) {
        //Name
    }
    public ArrayList<Route> GetUserPaths(String userinfo) {
        //Uid
        User u = parser.parseUser(userinfo);
        ArrayList<Route> r = new DBFunctions().getAllUserRoutes(u.getUid()); //Array of routes
        return r;
        //Presumably the array list can be later translated back into JSON
    }
    public void UpdateLoginTime(String userinfo) {
        //Parameters are uid
        User u = parser.parseUser(userinfo);
        u.setLastLogin(new Date()); //Assuming it's run immediately
    }
    public void UpdateExploration(String userinfo) {
        //Parameters are uid, amt of increase
        User u = parser.parseUser(userinfo);
        JSONParser p = new JSONParser();
        JSONObject obj = null;
        try{
            obj = (JSONObject) p.parse(userinfo);
        }
        catch(ParseException e) {
            System.exit(1);
        }
        int expl = (Integer) obj.get("expl");
        
        u.setRawExploration(u.getRawExploration() + expl);
    }
}
