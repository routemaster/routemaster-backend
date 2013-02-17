package routemaster.orm;

import com.mongodb.DBObject;

public interface IDocument {
    public DBObject toDBObject();
}
