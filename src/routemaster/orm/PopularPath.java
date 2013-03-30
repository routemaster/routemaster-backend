package routemaster.orm;

import com.mongodb.DBObject;
import com.mongodb.BasicDBObject;
import java.util.Date;

public class PopularPath implements IDocument {
    //Start and end geographic positions (order doesn't matter)
	private int ppid;
    private double startlt;
    private double startlg;
    private double endlt;
    private double endlg;
    //References to associated routes (using MongoDB ObjectIDs)
    private Route route;

    public PopularPath(DBObject base) {
        /*
        double[] start = new double[2];
        start = ((Number)base.get("start")).doubleValue();
        startlt = start[0];
        startlg = start[1];
        double[] end = new double[2];
        end = ((Number)base.get("end")).doubleValue();
        endlt = end[0];
        endlg = end[1];
        route = new Route((DBObject)base.get("route"));
        */
    }

    public PopularPath(double startlt, double startlg, double endlt,
            double endlg) {
        this.startlt = startlt;
        this.startlg = startlg;
        this.endlt = endlt;
        this.endlg = endlg;
    }

    public double getStartlt(){
        return startlt;
    }

    public double getStartlg() {
        return startlg;
    }

    public double getEndlt() {
        return endlt;
    }

    public double getEndlg() {
        return endlg;
    }

    public Route getRoute() {
        return route;
    }

    public DBObject toDBObject() {
        return new BasicDBObject().
            append("startlg", startlg).
            append("startlt", startlt).
            append("endlg", endlg).
            append("endlt", endlt).
            append("route", route);
    }

}
