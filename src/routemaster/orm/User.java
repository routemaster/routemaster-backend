package routemaster.orm;

import com.mongodb.DBObject;
import com.mongodb.BasicDBObject;
import java.util.Date;

public class User implements IDocument {
    private String name;
    private int uid;
    private Date registerDate;
    private Date lastLogin;
    private long rawExploration; // We might introduce a dividing factor

    public User(DBObject base) {
        name = (String)base.get("name");
        uid = ((Number)base.get("uid")).intValue();
        registerDate = (Date)base.get("registerDate");
        lastLogin = (Date)base.get("lastLogin");
        rawExploration = ((Number)base.get("rawExploration")).intValue();
    }

    // This is for user registration
    public User(String name, Counter counter) {
        this.name = name;
        uid = counter.getNext();
        registerDate = new Date();
        lastLogin = new Date();
        rawExploration = 0l;
    }

    public String getName() {
        return name;
    }

    public int getUid() {
        return uid;
    }

    public Date getRegisterDate() {
        return registerDate;
    }

    public Date getLastLogin() {
        return lastLogin;
    }

    public void setLastLogin(Date d) {
        lastLogin = d;
    }

    public long getRawExploration() {
        return rawExploration;
    }

    public void setRawExploration(long rawExploration) {
        this.rawExploration = rawExploration;
    }

    public DBObject toDBObject() {
        return new BasicDBObject().
            append("name", name).
            append("uid", uid).
            append("registerDate", registerDate).
            append("lastLogin", lastLogin).
            append("rawExploration", rawExploration);
    }
    
    public DBCursor createFromDB(int uid) {
        BasicDBObject query = new BasicDBObject("uid", uid);
        try{
            Orm o = new Orm();
        }
        catch(UnknownHostException e)
            System.exit(1);
        DBCursor db = o.getUsersCollection().find(query);
        return db;
        //return new User(db);
    }
}
