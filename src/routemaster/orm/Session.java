package routemaster.orm;

import com.mongodb.DBObject;
import com.mongodb.BasicDBObject;
import java.util.Date;

public Session implements IDocument() {
	//Timestamp
	private timestamp;
	//Long session UUID number
	private long uuid;
	//Associated short user id
	private int uid;
	
    public Session(DBObject base) {
        uuid = ((Number)base.get("uuid")).longValue();
        uid = ((Number)base.get("uid")).intValue();
        timestamp = (Date)base.get("timestamp");
    }
	
    //for new session
    public Session(long uuid, int uid) {
    	this.uuid = uuid;
    	this.uid = uid;
    	timestamp = new Date();
    }
	
	public long getUuid() {
		return uuid;
	}
	
	public int getUid() {
		return uid;
	}
	
	public Date getTimestamp() {
		return timestamp;
	}	
	
    public DBObject toDBObject() {
        return new BasicDBObject().
            append("uuid", uuid).
            append("uid", uid).
            append("timestamp", timestamp);
    }
}