package routemaster;
import java.io.IOException;
import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.server.Handler;
import javax.servlet.*;
import javax.servlet.http.*;  
import org.eclipse.jetty.server.handler.DefaultHandler;
import org.eclipse.jetty.server.handler.HandlerList;
import org.eclipse.jetty.server.handler.ResourceHandler;
import org.apache.log4j.Logger;
import org.apache.log4j.BasicConfigurator;
import org.apache.log4j.Level;

public class MyHandler extends DefaultHandler {
    
    public void handle(String target, HttpServletRequest request, 
        HttpServletResponse response, int dispatch) 
        throws IOException, ServletException
    {
        response.setContentType("text/html");
        response.setStatus(HttpServletResponse.SC_OK);
        response.getWriter().println("<h1>Hello OneHandler</h1>");
    }


}
