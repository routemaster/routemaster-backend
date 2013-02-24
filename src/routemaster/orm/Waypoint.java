package routemaster.orm;

import com.mongodb.DBObject;
import com.mongodb.BasicDBObject;
import java.util.Date;

//waypoints (2 letter names)
public class Waypoint implements IDocument {
    //Timestamp
    private Date ts;
    //Geographic position (latitude, longitude, and altitude)
    //what data type would this be?
    private double lt; //lat
    private double lg; //long
    private double al; //alt
    //Measurement accuracy (reported by the user's device)
    private double ac;
    //Associated route (using MongoDB ObjectIDs)
    private Route rt;
    //Associated short user id
    private int ui;

    public Waypoint(DBObject base) {
        ts = (Date)base.get("ts");
        /*
        double[] co = new double[2];
        co = ((Number)base.get("co")).doubleValue();
        lt = co[0];
        lg = co[1];
        */
        al = ((Number)base.get("al")).doubleValue();
        ac = ((Number)base.get("ac")).doubleValue();
        rt = (Route)base.get("rt");
        ui = ((Number)base.get("ui")).intValue();
    }

    public Waypoint(double lt, double lg, double al, int ui) {
        this.ui = ui;
        this.lt = lt;
        this.lg = lg;
        this. al = al;
        ts = new Date();
    }

    public Date getTs() {
        return ts;
    }

    public double getLt() {
        return lt;
    }

    public double getLg() {
        return lg;
    }

    public double getAl() {
        return al;
    }

    public double getAc() {
        return ac;
    }

    public Route getRt() {
        return rt;
    }

    public int getUi() {
        return ui;
    }

    public DBObject toDBObject() {
        return new BasicDBObject().
            append("ts", ts).
            append("lt", lt).
            append("lg", lg).
            append("al", al).
            append("ac", ac).
            append("ui", ui).
            append("rt", rt);
    }
}
