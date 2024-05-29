#accessing the elements of a table present in mysql
from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

## to get students information by name:
## ---->>>> TABLE WAS ALREADY MADE IN MYSQL(basic commands to check  the table status in vscode is in the video in our group)
## first : pip install flask mysql-connector-python
## second : saved this code and run it  by using python app2.py
## used thunder client  using get  request : chatgpt gave the URL


# Database connection
def create_db_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',      # Change this to your host
            user='root',           # Change this to your username
            password='resonance',  # Change this to your password
            database='day2updated'   # Change this to your database name
        )
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# API endpoint to get student data by name
@app.route('/student', methods=['GET'])
def get_student():
    name = request.args.get('Name')  # Adjusted to 'Name' with capital N
    connection = create_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    query = "SELECT * FROM svsp WHERE Name = %s"
    cursor.execute(query, (name,))
    result = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if result:
        return jsonify(result)
    else:
        return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
