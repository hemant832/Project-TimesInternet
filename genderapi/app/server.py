from flask import Flask,jsonify,request
from flask import render_template
#from flask_ngrok import run_with_ngrok
from returnprobability import returnprobability
import numpy as np
import pickle
from returngender import returngender
app=Flask(__name__)
#run_with_ngrok(app)
@app.route("/")
def hello():
	return "Hello"
@app.route("/gender")
def genderapi():
	c=request.args.get("name")
	gender=returngender(c)
	probability=returnprobability(c)
	return jsonify(Gender=gender,probability=probability)
if __name__=="__main__":
	app.run()