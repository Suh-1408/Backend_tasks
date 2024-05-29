#appending the table and calculating the avrage marks in the backend.
from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)


#for appending the table --> POST request with JSON--
# {
# "name": "John Doe",
#  "sub1": 85,
# "sub2": 90,
# "sub3": 95 }

# for  average marks simply get  request


# MySQL Configuration
mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'resonance',
    'database': 'day2updated',
    'auth_plugin': 'caching_sha2_password'
}

# Connect to MySQL
try:
    conn = mysql.connector.connect(**mysql_config)
    print("Connected to MySQL database")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")
    raise

# Endpoint to insert data into svsp table via API
@app.route('/insert_data', methods=['POST'])
def insert_data():
    data = request.get_json()
    name = data['name']
    sub1 = data['sub1']
    sub2 = data['sub2']
    sub3 = data['sub3']

    cursor = conn.cursor()
    insert_query = "INSERT INTO svsp (Name, sub1, sub2, sub3) VALUES (%s, %s, %s, %s)"
    cursor.execute(insert_query, (name, sub1, sub2, sub3))
    conn.commit()
    cursor.close()

    return jsonify({'message': 'Data inserted successfully'}), 201

# Endpoint to retrieve average marks for each Name
@app.route('/average_marks', methods=['GET'])
def average_marks():
    cursor = conn.cursor()
    avg_query = "SELECT Name, AVG((sub1 + sub2 + sub3)/3) AS average FROM svsp GROUP BY Name"
    cursor.execute(avg_query)
    results = cursor.fetchall()
    cursor.close()

    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)
