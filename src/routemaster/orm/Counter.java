package routemaster.orm;

import com.mongodb.DBObject;
import com.mongodb.BasicDBObject;
import com.mongodb.DBCollection;

public class Counter {
    private DBCollection collection;
    private String name;

    public Counter(DBCollection collection, String name) {
        this.collection = collection;
        this.name = name;
    }

    public void insert() {
    	if(collection.findOne(new BasicDBObject("_id", name)) != null) return;   	
    	
        collection.insert(new BasicDBObject().
        	append("_id", name).
            append("seq", 0));
    }
    
    public int getNext() {
    	return ((Number)collection.findAndModify(
    			new BasicDBObject("_id", name),
    		    new BasicDBObject("$inc", new BasicDBObject("seq", 1))
        ).get("seq")).intValue();
    }
}