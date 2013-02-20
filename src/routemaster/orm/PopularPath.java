package routemaster.orm;

import com.mongodb.DBObject;
import com.mongodb.BasicDBObject;
import java.util.Date;

public PopularPath implements IDocument {
	//Start and end geographic positions (order doesn’t matter)
	private double[] start;
	private double[] end;
	//References to associated routes (using MongoDB ObjectIDs)
	private Route route;
	
	public PopularPath(DBObject base) {
        double[] start = new double[2];
        start = ((Number)base.get("start")).doubleValue();
        double[] end = new double[2];
        end = ((Number)base.get("end")).doubleValue();
		route = (Route)base.get("route");
	}
	
	public PopularPath(double[] start, double[] end) {
		this.start = start;
		this.end = end;
	}
	
	public double[] getStart(){
		return start;
	}
	
	public double[] getEnd() {
		return end;
	}
	
	public Route getRoute() {
		return route;
	}
	//set?	
	
    public DBObject toDBObject() {
        return new BasicDBObject().
            append("start", start).
            append("end", end).
            append("route", route);
    }
}