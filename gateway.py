from flask import Flask, request, jsonify
import requests
import sqlite3
app = Flask(__name__)
data = {
    'data': ' *\n **\n***\n****\n'
}
conn = sqlite3.connect('results.db')
c = conn.cursor()

# Create a table to store the results
c.execute('''CREATE TABLE results
             (id INTEGER PRIMARY KEY AUTOINCREMENT, service TEXT, result TEXT)''')

conn.commit()
conn.close()

response = requests.post('http://localhost:5000/service1', json=data)
print(response.json())
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        rows = data['data'].split('\n')
        col1 = [row[0:2] for row in rows]
        # Concatenate the strings in reverse order
        result = '\n'.join(col1[::-1])
        # Store the result in the database
        conn = sqlite3.connect('results.db')
        c = conn.cursor()
        c.execute("INSERT INTO results (service, result) VALUES (?, ?)", ('Service 1', result))
        conn.commit()
        conn.close()
        return jsonify({'result': result})
    else:
        return 'Service 1 GET endpoint'
    
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.json
        rows = data['data'].split('\n')
        col1 = [row[0:2] for row in rows]
        # Concatenate the strings in reverse order
        result = '\n'.join(col1[::-1])
        # Store the result in the database
        conn = sqlite3.connect('results.db')
        c = conn.cursor()
        c.execute("INSERT INTO results (service, result) VALUES (?, ?)", ('Service 1', result))
        conn.commit()
        conn.close()
        return jsonify({'result': result})
    else:
        return 'Service 1 GET endpoint'
conn = sqlite3.connect('results.db')
c = conn.cursor()

# Retrieve all the results from the database
c.execute("SELECT * FROM results")
results = c.fetchall()

for result in results:
    print(result)

conn.close()