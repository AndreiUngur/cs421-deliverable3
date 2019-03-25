from flask import Flask, request, jsonify, make_response
from sqlalchemy import create_engine
from flask_cors import CORS, cross_origin
from utils import app, db
from games import get_games, add_gamelisting
from payment import add_payment_method
from users import add_dev, find_dev

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
  content = request.form
  if not content:
       return "<h1> Error! </h1><p>You need some form content</p>"
  username, password = content.get("username"), content.get("password")
  email, studio = content.get("email"), content.get("studio")
  developer_from_db = find_dev(username)
  if developer_from_db:
       return "<h1> Error! </h1> Your username already has a developer account!"
  return add_dev(username, password, email, studio)


@app.route("/create/game", methods=["POST"])
@cross_origin()
def add_gamelisting_endpoint():
  content = request.form
  if not content:
       return jsonify({"status": "You need some form content"})
  game_name, game_desc, price, category = content.get("title"), content.get("description"), content.get("price"), content.get("category")
  is_on_sale, sale_price = content.get("is_on_sale"), content.get("sale_price")
  if is_on_sale.lower() == 'yes':
       is_on_sale = True
  else:
       is_on_sale = False
  developer = content.get("developer")
  developer_from_db = find_dev(developer)
  if not developer_from_db:
       return jsonify({"status": "The developer you specified doesn't exist! Please create the account."})
  return add_gamelisting(game_name, game_desc, is_on_sale, price, category, sale_price, developer)

@app.route('/create/paymentmethod')
@cross_origin()
def add_payment_method_endpoint():
  content = request.json
  return jsonify(add_payment_method())

if __name__ == '__main__':
  app.run(port=port)
