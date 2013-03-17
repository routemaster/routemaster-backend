package routemaster;
import java.io.IOException;
import org.eclipse.jetty.server.Server;

public class JsonServer extends Server {
    public JsonServer(int port) {
        super(port);
        setHandler(new MyHandler());
    }

    public static void main(String[] args) throws Exception {
        JsonServer server = new JsonServer(
            args.length == 0 ? 8080 : Integer.parseInt(args[0]));
        server.start();
        server.join();
    }
}
