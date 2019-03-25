from flask import Flask, request, jsonify, make_response
from sqlalchemy import create_engine
from flask_cors import CORS, cross_origin
from utils import app, db
from games import get_games, add_gamelisting
from payment import add_payment_method
from users import add_dev

CORS(app)

port = 4293
@app.route('/')
def index():
    return "Hello world!"

@app.route('/games')
@cross_origin()
def get_games_endpoint():
     return jsonify(get_games())


@app.route("/create/dev", methods=["POST"])
@cross_origin()
def add_developer_endpoint():
    content = request.json
    if not content:
        return jsonify({"status": "You need a JSON body"})
    username, password = content.get("username"), content.get("password")
    email, studio = content.get("email"), content.get("studio")
    return jsonify(add_dev(username, password, email, studio))


@app.route("/create/game", methods=["POST"])
@cross_origin()
def add_gamelisting_endpoint():
    content = request.json
    if not content:
        return jsonify({"status": "You need a JSON body"})
    game_name, game_desc, price, category = content.get("title"), content.get("description"), content.get("price"), content.get("category")
    is_on_sale, sale_price = content.get("is_on_sale"), content.get("sale_price")
    developer = content.get("developer")
    return jsonify(add_gamelisting(game_name, game_desc, is_on_sale, price, category, sale_price, developer))

@app.route('/create/paymentmethod')
@cross_origin()
def add_payment_method_endpoint():
    content = request.json
    return jsonify(add_payment_method())

if __name__ == '__main__':
     app.run(port=port)
