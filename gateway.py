import requests
from flask import g
from flask import Flask, request, jsonify
from sqlalchemy.orm import Session
from sqlalchemy import select
from model import engine, DataStore

app = Flask(__name__)
SERVICES = ["http://127.0.0.1:5001/", "http://127.0.0.1:5002/"]

with app.app_context():
    g.REQ_ID = 0


def service_limited_counter(counter):
    if counter == len(SERVICES) - 1:
        return 0
    return counter + 1


def parse_body(body):
    body = body.decode("utf-8").replace("\r", "").replace(" ", "").replace("'", "").replace("{", "").replace("}", "").split("\n")
    return body


@app.route("/", methods=["GET", "POST"])
def default_route():
    resp_body = "{'"
    if request.method == "POST":
        req_body = parse_body(request.data)
        req_len = len(req_body)
        count = 0
        for to_send in req_body:
            requests.post(SERVICES[count], to_send)
            count = service_limited_counter(count)

        with Session(engine) as session:
            data = select(DataStore).order_by(DataStore.id.desc()).limit(req_len)

            for el in session.scalars(data):
                resp_body += str(el) + "\n"
        resp_body += "'}"

        return resp_body

    if request.method == "GET":
        return jsonify({"msg_get": "gateway-get"})


if __name__ == "__main__":
    app.run(debug=True)
