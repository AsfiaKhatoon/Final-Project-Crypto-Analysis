from flask import Flask, render_template 
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os 
#from prediction import predict

# create app 
app = Flask(__name__)

# create database engine 
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_SERVER_NAME = os.environ.get("DB_SERVER_NAME")
DB_DATABASE_NAME = os.environ.get("DB_DATABASE_NAME")

connection_url = URL.create(
    drivername = "postgresql+pg8000", 
    username = DB_USER,
    password = DB_PASSWORD,
    host = DB_SERVER_NAME, 
    port = 5432,
    database = DB_DATABASE_NAME, 
)

engine = create_engine(connection_url)

# page routes

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/Analysis")
def Analysis():
    return render_template("Analysis.html")

@app.route("/Prediction")
def Prediction():
    return render_template("Prediction.html")

@app.route("/Problem")
def The_Problem():
    return render_template("Problem.html")

if __name__ == "__main__":
    app.run(debug=True)