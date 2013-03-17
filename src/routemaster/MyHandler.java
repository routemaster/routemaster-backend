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
        response.setContentType("application/json");
        response.setStatus(HttpServletResponse.SC_OK);
        baseRequest.setHandled(true);
        PrintWriter out = response.getWriter();
        HttpURI uri = baseRequest.getUri();
        String path = uri.getDecodedPath();
        // Parse the URI
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
        else {
            out.println("Hello y'all!");
            out.println("The uri you requested was: " + path);
            out.println("Try requesting a uri like /user/3");
        }
    }
}
