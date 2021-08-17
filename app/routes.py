from app import app
from flask import Response, request, jsonify, abort

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/')
def index():
    return 'index'
    app = Flask(__name__, instance_relative_config=True)
    if test_config:
        # load test config
        app.config.from_mapping(test_config)


@app.before_request
def log_before_request():
    print('\n-------------------------------------------------------------------')

@app.after_request
def log_after_request(response):
    print('-------------------------------------------------------------------')
    return response

