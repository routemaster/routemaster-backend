package routemaster.orm;

import com.mongodb.DBObject;
import com.mongodb.BasicDBObject;
import java.util.Date;

//waypoints (2 letter names)
public Waypoint implements IDocument {
	//Timestamp
	private Date ts;
	//Geographic position (latitude, longitude, and altitude)
	//what data type would this be?
	private lt; //lat
	private lg; //long
	private al; //alt
	//Measurement accuracy (reported by the user’s device)
	private float ac;
	//Associated route (using MongoDB ObjectIDs)
	private rt;
	//Associated short user id
	private int ui;
	
	public Waypoint(DBObject base) {
        ts = (Date)base.get("ts");
        lt = ()base.get("lt");
        lg = ()base.get("lg");
        al = ()base.get("al");
        ac = ((Number)base.get("ac")).floatValue();
        rt = ()base.get("rt");
        ui = ((Number)base.get("ui")).intValue();
	}
	
	public Waypoint(int ui) {
        this.ui = ui;
        ts = new Date();      
	}
	
	public Date getTs() {
		return ts;
	}
	
	public __ getLt() {
		return lt;
	}
	
	public __ getLg() {
		return lg;
	}
	
	public __ getAl() {
		return al;
	}
	
	public flaot getAc() {
		return ac;
	}
	
	public __ getRt() {
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
            append("rc", rc);
    }
}