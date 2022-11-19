import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template

#################################################
# Database Setup
#################################################
SQL_Password = input('Please enter your localhost Postgresql password: ')
#password = SQL_Password
DB_Name = 'FlightDB'

# create engine, connect to postgresql DB
engine = create_engine(f'postgresql://postgres:{SQL_Password}@localhost/{DB_Name}')

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Airline = Base.classes.airline
Location = Base.classes.location
SeatClass = Base.classes.seatclass
Stop = Base.classes.stop
Flight = Base.classes.flight
FlightClass = Base.classes.flight_class

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/")
def welcome():
    # List all available api routes
    return (
        f"Available routes:<br/>"
        f"/api/v1.0/airlines<br/>"
        f"/api/v1.0/seatclass<br/>"
        f"/api/v1.0/locations<br/>"
        f"/api/v1.0/stops"
    )

# @app.route("/api/v1.0/airlines")
# def welcome():
#     # Create session link from Python to DB
#     session = Session(engine)

#     # return airlines SQL data
#     results = engine.execute("SELECT airlineid, airline, designator \
#                             FROM public.airline ORDER BY airlineid;").all()

#     session.close()



#################################################
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)