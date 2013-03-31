package routemaster;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.ServletException;
import org.eclipse.jetty.http.HttpURI;
import org.eclipse.jetty.server.handler.AbstractHandler;
import org.eclipse.jetty.server.Request;

import com.mongodb.DBCursor;
import com.mongodb.DBObject;
import routemaster.jrm.ConvertToJSON;
import routemaster.jrm.DBFunctions;
import routemaster.orm.User;

public class MyHandler extends AbstractHandler {
    public void handle(String target, Request baseRequest,
        HttpServletRequest request, HttpServletResponse response)
        throws IOException, ServletException
    {
        //Sachit: Here I attempt to determine if this is a request
        //with JSON data (PUT or POST). Idk if using a try/catch 
        //here is the best idea...
        boolean isPUTPOST = false;
        try {
            //if this section returns an error, try 
            //getInputStream() instead on the request
            //i.e. br.getInputStream()
            BufferedReader br = hsr.getReader();  <<< Exception
            String jsonString = br.readLine();
            if ((jsonString == null) || jsonString.isEmpty()) {
                log.error("Request not POST w/ JSON");
            } 
            else {
                log.info("JSON from POST is:" + jsonString);
                isPUTPOST = true;
            }
        } 
        catch (IOException ex) {
            log.error(ex.toString());
        }
        response.setContentType("application/json");
        response.setStatus(HttpServletResponse.SC_OK);
        baseRequest.setHandled(true);
        PrintWriter out = response.getWriter();
        HttpURI uri = baseRequest.getUri();
        String path = uri.getDecodedPath();
        // Parse the URI for no JSON
        if (isPUTPOST == false)
        {
            if (path.startsWith("/user/")) {
                int userid = Integer.parseInt(path.substring(6));
                // Get a user from the database
                DBFunctions dbf = new DBFunctions();
                DBCursor db = dbf.getUserFromDB(userid);
                DBObject dbobj = db.next();
                User user = new User(dbobj);
                ConvertToJSON ctj = new ConvertToJSON();
                String userJSON = ctj.convertUser(user).toString();
                out.println(userJSON);
            }
            else if (path.startsWith("/leader/efficiency")) {
                //DB leader efficiency code
            }
            else if (path.startsWith("/leader/exploration")) {
                //DB leader exploration code
            }
            else if (path.startsWith("/recent/user")) {
                int userid = Integer.parseInt(path.substring(12));
                // Get a user from the database
                DBFunctions dbf = new DBFunctions();
                DBCursor db = dbf.getAllUserRoutes(userid);
                DBObject dbobj = db.next();
                User user = new User(dbobj);
                ConvertToJSON ctj = new ConvertToJSON();
                String userJSON = ctj.convertUser(user).toString();
                out.println(userJSON);
            }
            else if (path.startsWith("/popularpath/") {
                //Not sure what this one does
            }
            else if (path.startsWith("/namesuggestions/")  {
                //Here I use the request.getParameter() tool to fetch the lat an
                //d long.
                //e.g. if the URI were namesuggestions/startlatitude=420&startlo
                //ngitude=420&endlatitude=520&endlongitude=520
                //Parse the parameters
                double startlatitude = 
                    Double.parseDouble(request.getParameter("startlatitude"));
                double startlongitude = 
                    Double.parseDouble(request.getParameter("startlongitude"));
                double endlatitude = 
                    Double.parseDouble(request.getParameter("endlatitude"));
                double endlongitude = 
                    Double.parseDouble(request.getParameter("endlongitude"));
                // Get the name suggestions
                DBFunctions dbf = new DBFunctions();
                DBCursor db = dbf.getPPathsFromDB(startlatitude,
                    startlongitude,endlatitude,endlongitude);
                DBObject dbobj = db.next();
                User user = new User(dbobj);
                ConvertToJSON ctj = new ConvertToJSON();
                String userJSON = ctj.convertUser(user).toString();
                out.println(userJSON);
            else {
                out.println("Hello y'all! You submitted a request w/ no JSON");
                out.println("The uri you requested was: " + path);
                out.println("Try requesting a uri like /user/3");
            }
        }
        
        //Parse for JSON included requests
        else if (isPUTPOST == true)
        {
            if (path.startswith("/user/")){
                
            }
            else {
                out.println("Hello y'all! You submitted a request w/ JSON");
                out.println("The uri you requested was: " + path);
                out.println("Try requesting a uri like /user/3");
            }
        }
    }
}
