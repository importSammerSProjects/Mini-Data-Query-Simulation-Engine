from flask import Flask, request, jsonify
from auth import generate_token, token_required
from utils import process_query, explain_query, validate_query

app = Flask(__name__)

# Endpoint to generate JWT token
@app.route('/token', methods=['POST'])
def get_token():
    data = request.json
    if not data or 'username' not in data:
        return jsonify({'error': 'Username is required'}), 400
    token = generate_token(data['username'])
    return jsonify({'token': token})

# Introduction
@app.route('/', methods=['POST', 'Get'])
def intro():
    return 'Welcome to the Mini Data Query Simulation Engine \n Project by Sameer Najir Sayyed'

# Protected route: Simulate AI-powered query processing
@app.route('/query', methods=['POST'])
@token_required
def query(current_user):
    data = request.json
    print(request.json)
    if not data or 'query' not in data:
        return jsonify({'error': 'Query is required'}), 400
    response = process_query(data['query'])
    return jsonify({'user': current_user, 'query_result': response})

# Protected route: Returns simulated query breakdown
@app.route('/explain', methods=['POST'])
@token_required
def explain(current_user):
    data = request.json
    if not data or 'query' not in data:
        return jsonify({'error': 'Query is required'}), 400
    explanation = explain_query(data['query'])
    return jsonify({'user': current_user, 'explanation': explanation})

# Protected route: Checks query feasibility
@app.route('/validate', methods=['POST'])
@token_required
def validate(current_user):
    data = request.json
    if not data or 'query' not in data:
        return jsonify({'error': 'Query is required'}), 400
    is_valid = validate_query(data['query'])
    return jsonify({'user': current_user, 'valid': is_valid})

if __name__ == '__main__':
    app.run(debug=True)
