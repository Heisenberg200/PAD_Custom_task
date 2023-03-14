from flask import Flask, request, jsonify
from sqlalchemy.orm import Session

from model import engine, DataStore

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def default_route():
    if request.method == "POST":
        body = request.data.decode()

        with Session(engine) as session:
            data = DataStore(name=body)
            session.add(data)
            session.commit()

        return jsonify({"service2": body})

    if request.method == "GET":
        return jsonify({"service2": "get-req"})


if __name__ == "__main__":
    app.run(debug=True, port=5002)
