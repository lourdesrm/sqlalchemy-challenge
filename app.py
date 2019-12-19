# Import Flask
import numpy as np
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import func
from sqlalchemy import create_engine
import datetime as dt
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create an app
app = Flask(__name__)


# Define available routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/startdate<br/>"
        f"/api/v1.0/enddate<br/>"
)

# Precipitation dictionary
@app.route("/api/v1.0/precipitation")
def names():
    """Return a list of all passenger names"""

    # # Query all passengers
    # session = Session(engine)
    # results = session.query(Passenger.name).all()

    # # close the session to end the communication with the database
    # session.close()

    # # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    # return jsonify(all_names)


# List of stations
@app.route("/api/v1.0/station")
def stations():
    """Return a list of stations"""

    # Query all passengers
    session = Session(engine)
    station_total = session.query(Measurement.station.distinct()).all()

    # close the session to end the communication with the database
    session.close()

    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))

    return jsonify(station_total)


# Observations of temperatures in 12 mo
@app.route("/api/v1.0/tobs")
def temp():
    """Return a list of temperatures"""

    # Query all passengers
    session = Session(engine)
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Execute Query
    prcp_12mo = session.query(Measurement.tobs).filter(Measurement.date > query_date).all()

    # close the session to end the communication with the database
    session.close()

    return jsonify(prcp_12mo)



# Observations of temperatures for given start date
@app.route("/api/v1.0/startdate")
def start():
    """Return a list of temperatures"""

    # Query all passengers
    session = Session(engine)
    start_date = '2017-07-05'
    
    # Execute Query
    max_tobs = (session.query(func.max(Measurement.tobs))).filter(Measurement.date >= start_date).all()
    min_tobs = (session.query(func.min(Measurement.tobs))).filter(Measurement.date >= start_date).all()
    avg_tobs = (session.query(func.avg(Measurement.tobs))).filter(Measurement.date >= start_date).all()
    # close the session to end the communication with the database
    session.close()

    all_temperatures = {
        "Maximum Temperature" : max_tobs,
        "Minimum Temperature": min_tobs,
        "Average Temperature": avg_tobs
    }

    return jsonify(all_temperatures)

#Observations of temperatures for given start date - end date
@app.route("/api/v1.0/enddate")
def end():
    """Return a list of temperatures between given dates"""

    # Query all passengers
    session = Session(engine)
    start_date = '2017-07-05'
    end_date = '2017-07-15'
    
    # Execute Query
    max_tobs_2 = (session.query(func.max(Measurement.tobs))).filter(Measurement.date > start_date).filter(Measurement.date < end_date).all()
    min_tobs_2 = (session.query(func.min(Measurement.tobs))).filter(Measurement.date > start_date).filter(Measurement.date < end_date).all()
    avg_tobs_2 = (session.query(func.avg(Measurement.tobs))).filter(Measurement.date > start_date).filter(Measurement.date < end_date).all()
    # close the session to end the communication with the database
    session.close()

    all_temperatures_2 = {
        "Maximum Temperature" : max_tobs_2,
        "Minimum Temperature": min_tobs_2,
        "Average Temperature": avg_tobs_2
    }

    return jsonify(all_temperatures_2)


if __name__ == "__main__":
    app.run(debug=True)


