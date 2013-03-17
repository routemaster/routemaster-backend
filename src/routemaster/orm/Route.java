package routemaster.orm;

import com.mongodb.DBObject;
import com.mongodb.DBCursor;
import com.mongodb.BasicDBObject;
import java.util.Date;

//Routes (4 letter names)
public class Route implements IDocument {
    //List of waypoints
    //private Waypoint wypt[];
    //Start and end timestamps
    private Date stts;
    private Date edts;
    //Associated short user id
    private int uid;
    //Efficiency score
    private int effs;
    //Disqualified flag...if disqualified, set to true
    private boolean disq;

    public Route(DBObject base) {
        // wypt = new Waypoint((DBObject)base.get("wypt"));
        stts = (Date)base.get("stts");
        edts = (Date)base.get("edts");
        uid = ((Number)base.get("uid")).intValue();
        effs = ((Number)base.get("effs")).intValue();
        disq = (Boolean)base.get("disq");
    }

    public Route(int uid) {
        this.uid = uid;
        stts = new Date();
        edts = new Date();
        effs = 0;
        disq = false;
    }

    /*public Waypoint getWypt() {
        return wypt;
    }
    */
    public Date getStts() {
        return stts;
    }

    public Date getEdts() {
        return edts;
    }

    public int getUid() {
        return uid;
    }

    public int getEffs() {
        return effs;
    }

    public boolean getDisq(){
        return disq;
    }

    /*public void addWypt(Waypoint w) {

    }
    */
    public void setStts(Date d) {
        stts = d;
    }

    public void setEdts(Date d){
        edts = d;
    }

    public void setEffs(int effs) {
        this.effs = effs;
    }

    public void setDisq(boolean disq) {
        this.disq = disq;
    }

    public DBObject toDBObject() {
        return new BasicDBObject().
            //append("wypt", wypt).
            append("stts", stts).
            append("edts", edts).
            append("uid", uid).
            append("effs", effs).
            append("disq", disq);
    }

}
