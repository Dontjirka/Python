# first install flask using "pip install flask"
# then run flask using "flask run"
# then run this app
# then go to "http://127.0.0.1:5000/"
from urllib import response
from flask import Flask, request, jsonify
import json
import hashlib

#######################################################
# digital signature for request
def create_signature(request):
    message = request.method + request.path
    signature = hashlib.sha256(message.encode()).hexdigest()
    return signature
#######################################################

#######################################################
#digital signature for response
def create_signature(response):
    message = str(response.status_code) + response.get_data(as_text=True)
    signature = hashlib.sha256(message.encode()).hexdigest()
    return signature
#######################################################

signature = create_signature(request)
response.headers['X-Signature'] = signature

signature = create_signature(response)
response.headers['X-Signature'] = signature

#######################################################
# verify signature
def verify_signature(request_or_response):
    signature = request_or_response.headers.get('X-Signature')

    if hasattr(request_or_response, 'method'):
        message = request_or_response.method + request_or_response.path
    else:
        message = str(request_or_response.status_code) + request_or_response.get_data(as_text=True)

    calculated_signature = hashlib.sha256(message.encode()).hexdigest()

    if signature == calculated_signature:
        return {'status': 'ok'}
    else:
        return {'status': 'invalid'}
#######################################################

#######################################################
app = Flask(__name__)
#endpoint 1
@app.route('/add')
def add():
    a = request.args.get('a')
    b = request.args.get('b')
    try:
        result = int(a) + int(b)
    except ValueError:
        return jsonify({'status': 'error', 'message': 'Invalid parameters'})

    # save result to a JSON file
    with open('results.json', 'w') as f:
        json.dump({'status': 'ok', 'result': result}, f)

    return jsonify({'status': 'ok', 'result': result})

#endpoint 2
@app.route('/subtract')
def subtract():
    a = request.args.get('a')
    b = request.args.get('b')
    try:
        result = int(a) - int(b)
    except ValueError:
        return jsonify({'status': 'error', 'message': 'Invalid parameters'})

    # save result to a JSON file
    with open('results.json', 'w') as f:
        json.dump({'status': 'ok', 'result': result}, f)

    return jsonify({'status': 'ok', 'result': result})
#######################################################

if __name__ == '__main__':
    app.run()