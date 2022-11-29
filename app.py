# include ------------------------------------------------------------------------
from flask import Flask, render_template, request, jsonify
import pickle
#import numpy as np
#import collections

# initialize ---------------------------------------------------------------------
app = Flask(__name__, static_folder='assets')

# Load the model back from file in the current working directory
pickle_filename = "Model_KNN.pkl"  
with open(pickle_filename, 'rb') as file: clf = pickle.load(file)

# flight price inits
current_fuel_price = 3.198
mins = 580

# root route ---------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

# predict route ------------------------------------------------------------------
@app.route("/predict", methods=['GET','POST'])
def predict():
    dataInput = (request.json)
    
    x_in = [dataInput['airline'], dataInput['from_loc'], dataInput['to_loc'], mins, dataInput['seatclass'], dataInput['depart'], dataInput['arrive'], dataInput['stop'], current_fuel_price]

    # Use the fitted model to predict the y-value of the sample
    y_pred = clf.predict([x_in])

    # Return predicted value
    return jsonify({"ticketprice": y_pred[0][0]})

# turn off cache -----------------------------------------------------------------
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

# --------------------------------------------------------------------------------
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)