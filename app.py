# hello world api and counting no of letters present.
from flask import Flask, request, jsonify
from collections import Counter
import string

app = Flask(__name__)
# pehle pip install flask se flask ka installation.
# fir ye app.py wala code likha 
# fir python app.py
# fir thunderclient pe accordingly karna tha.
# baar baar virtual env set krne ki zaroorat ni padti

# Basic "Hello, World!" route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Route to count alphabets in a string
@app.route('/count_alphabets', methods=['POST'])
def count_alphabets():
    data = request.get_json()
    input_string = data.get('input_string', '')
    
    # Filter only alphabetic characters and convert them to lower case
    filtered_string = ''.join(filter(str.isalpha, input_string)).lower()
    
    # Count the occurrence of each alphabet
    counts = Counter(filtered_string)
    
    # Convert counts to a dictionary
    result = {char: counts[char] for char in string.ascii_lowercase if counts[char] > 0}
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
