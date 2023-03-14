from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
app = Flask(__name__)
 
 
@app.route("/", methods=["GET", "POST"])
def default_route():
    if request.method == "POST":
        return jsonify({"msg_post": "hi from service 2"})
 
    if request.method == "GET":
        return jsonify({"msg_get": "hi from service 2"})
 
 
if __name__ == "__main__":
    app.run(port=5002)