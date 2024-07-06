# Import the dependencies.
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)
# Find the most recent date in the data set to be used in other queries.
most_recent_date_query = session.query(func.max(measurement.date))
most_recent_date = most_recent_date_query[0][0]
m_r_d_actual = dt.date.fromisoformat(most_recent_date) # convert the date string into a date object.

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    return jsonify()

@app.route("/api/v1.0/stations")
def stations():
    # Get all the data from the stations table.
    stations_query = session.query(station.station, station.name, station.latitude, station.longitude, station.elevation).all()
    return jsonify([{"station":stat, "name":name, "latitude":lat, "longitude":long, "elevation":elev} 
                    for stat, name, lat, long, elev in stations_query])

@app.route("/api/v1.0/tobs")
def tobs():
    # Calculate the date one year from the last date in data set.
    query_date_range = m_r_d_actual.replace(year=m_r_d_actual.year-1).isoformat()

    # Query to find the most active station (i.e. which stations had the most rows?)
    # List all the stations and their row counts in descending order and get the station id of the first station in the query.
    most_active_station_query = session.query(measurement.station, func.count(measurement.station)).\
    group_by(measurement.station).\
        order_by(sqlalchemy.desc(func.count(measurement.station)))[0][0]
    # The criteria needed to filter out all the stations except for the most active station id from the previous query.
    criteria = measurement.station == most_active_station_query

    # Query the last 12 months of temperature observation data for this station the most active station
    tobs_query = session.query(measurement.date, measurement.tobs).\
        filter(measurement.date >= query_date_range, criteria)
    return jsonify([{"date":dat, "temperature observation":tob} for dat, tob in tobs_query])

@app.route("/api/v1.0/<start>/<end>")
def tobs_agg(start:str, end=most_recent_date):
    # Remove any spaces in the start and end dates entered.
    start = start.replace(" ", "")
    end = end.replace(" ", "")

    # Using the most active station id from the previous query, calculate the lowest, highest, and average temperature.
    temp_agg_query = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
        filter(measurement.date >= start, measurement.date <= end)
    return jsonify([{"minimum":min, "maximum":max, "average":avg} for min, max, avg in temp_agg_query])

@app.route("/api/v1.0/<start>")
def call_tobs_agg(start:str):
    return tobs_agg(start=start)

session.close()