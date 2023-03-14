import requests
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
 
app = Flask(__name__)
SERVICES = ["http://127.0.0.1:5001/", "http://127.0.0.1:5002/"]
 
 
@app.route("/", methods=["GET", "POST"])
def default_route():
    body = []
    if request.method == "POST":
        for url in SERVICES:
            resp = requests.post(url, data=request.data)
            body.append(resp.text)
        return jsonify({"msg_post": body})
 
    if request.method == "GET":
        for url in SERVICES:
            resp = requests.get(url)
            body.append(resp.text)
        return jsonify({"msg_get": body})
 
 
if __name__ == "__main__":
    app.run(debug=True)