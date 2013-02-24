import org.testng.annotations.*;
import routemaster.orm.*;
import com.mongodb.MongoClient;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.BasicDBObject;
import com.mongodb.DBObject;
import java.net.UnknownHostException;

public class UserTest {
    private Orm orm;
    private Counter counter;
    private User l;
    private User c;
    private User b;

    @BeforeClass
    public void setUp() throws UnknownHostException {
        orm = new Orm();
        counter = new Counter(orm.getUsersCollection(), "users");
        counter.insert();
        l = new User("Lauren", counter);
        c = new User("Colin", counter);
        b = new User("Ben", counter);
    }

    @Test
    public void testUID() {
        assert l.getUid() != c.getUid();
        assert l.getUid() != b.getUid();
        assert c.getUid() != b.getUid();
    }

    @Test
    public void testInAndOut() {
        DBObject lDB = l.toDBObject();
        DBCollection coll = orm.getUsersCollection();
        coll.insert(lDB);

        DBObject query = new BasicDBObject("name", "Lauren");
        DBObject myDoc = coll.findOne(query);

        User newL = new User(myDoc);

        assert l.getUid() != newL.getUid();
    }
}
