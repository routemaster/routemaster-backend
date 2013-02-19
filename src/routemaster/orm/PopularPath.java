package routemaster.orm;

import com.mongodb.DBObject;
import com.mongodb.BasicDBObject;
import java.util.Date;

public PopularPath implements IDocument {
	//Start and end geographic positions (order doesn’t matter)
	private start;
	private end;
	//References to associated routes (using MongoDB ObjectIDs)
	private Route route;
	
	public PopularPath(DBObject base) {
		
		
	}
	
	public PopularPath() {
		
		
	}
	
	//get
	//set
	
	
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