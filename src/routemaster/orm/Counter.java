package routemaster.orm;

import com.mongodb.DBObject;

public class Counter {
    private Collection collection;
    private String name;

    // TODO:
    // http://docs.mongodb.org/manual/tutorial/create-an-auto-incrementing-field

    public Counter(Collection collection, String name) {
        this.collection = collection;
        this.name = name;
    }

    public void insert() {
        collection.insert(new DBObject().
        	append("_id", name);
            append("seq", 0));
    }
    
    public void getNext() {
    	return ((Number)collection.findAndModify(
    		new DBObject().
    			append("query", new DBObject("_id", name).
    		    append("update", new DBObject("$inc", new DBObject("seq", 1))).
    		    append("new", true);
        ).get("seq")).intValue();
    }
}