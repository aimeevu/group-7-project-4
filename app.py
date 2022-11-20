import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import psycopg2
from flask import Flask, jsonify, render_template

#################################################
# Database Setup
#################################################
SQL_Password = input('Please enter your localhost Postgresql password: ')

DB_Name = 'FlightDB'

conn_string = f"host='localhost' dbname='FlightDB' user='postgres' password='{SQL_Password}'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

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
def test():
    # results = cursor.execute('SELECT public."Agency".agency_name, CAST(sum(public."Offense".cleared) as bigint),\
    #      CAST(sum(public."Offense".actual) as bigint) FROM public."Agency" Left Join public."Offense" \
    #         on public."Offense".ori = public."Agency".ori where public."Offense".actual is not null \
    #             group by public."Agency".agency_name;')
    # rows = cursor.fetchall()
    results = cursor.execute("SELECT airlineid, airline, designator \
                            FROM public.airline ORDER BY airlineid;")
    rows = cursor.fetchall()
    for row in rows:
        d = collections.OrderedDict()
        d['airlineid'] = row[0]
        d['airline'] = row[1]
        d['designator'] = row[2]

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route("/")
# def welcome():
#     # List all available api routes
#     return (
#         f"Available routes:<br/>"
#         f"/api/v1.0/airlines<br/>"
#         f"/api/v1.0/seatclass<br/>"
#         f"/api/v1.0/locations<br/>"
#         f"/api/v1.0/stops"
#     )

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