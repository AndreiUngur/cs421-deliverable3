from flask import Flask, request, jsonify, make_response
from sqlalchemy import create_engine
from flask_cors import CORS, cross_origin
from utils import app, db
from games import get_games, add_gamelisting
from payment import add_payment_method

CORS(app)

port = 4293
@app.route('/')
def index():
    return "Hello world!"

@app.route('/games')
@cross_origin()
def get_games_endpoint():
     return jsonify(get_games())

@app.route("/add/game", methods=["POST"])
@cross_origin()
def add_gamelisting_endpoint():
    content = request.json
    return jsonify(add_gamelisting())

@app.route('/add/paymentmethod')
@cross_origin()
def add_payment_method_endpoint():
    content = request.json
    return jsonify(add_payment_method())

if __name__ == '__main__':
     app.run(port=port)
