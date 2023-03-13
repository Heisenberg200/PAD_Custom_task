from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

engine = create_engine('sqlite:///results.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    service = Column(String)
    result = Column(String)

    def __repr__(self):
        return f"<Result(id={self.id}, service='{self.service}', result='{self.result}')>"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        rows = data['data'].split('\n')
        col1 = [row[0:2] for row in rows]
        # Concatenate the strings in reverse order
        result = '\n'.join(col1[::-1])
        # Store the result in the database
        with Session() as session:
            result_obj = Result(service='Service 1', result=result)
            session.add(result_obj)
            session.commit()
        return jsonify({'result': result})
    else:
        return 'Service 1 GET endpoint'

@app.route('/service2', methods=['GET', 'POST'])
def service2():
    if request.method == 'POST':
        data = request.json
        rows = data['data'].split('\n')
        col2 = [row[2:4] for row in rows]
        # Concatenate the strings in reverse order
        result = '\n'.join(col2[::-1])
        # Store the result in the database
        with Session() as session:
            result_obj = Result(service='Service 2', result=result)
            session.add(result_obj)
            session.commit()
        return jsonify({'result': result})
    else:
        return 'Service 2 GET endpoint'

@app.route('/results', methods=['GET'])
def results():
    with Session() as session:
        results = session.query(Result).all()
        result_list = []
        for result in results:
            result_list.append({'id': result.id, 'service': result.service, 'result': result.result})
        return jsonify(result_list)

if __name__ == '__main__':
    app.run(debug=True)