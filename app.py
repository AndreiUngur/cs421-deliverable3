#!/usr/bin/env python3

from flask import Flask, request, make_response
from sqlalchemy import create_engine
from flask_cors import CORS, cross_origin
from utils import app, db, tunnel
from games import add_gamelisting, show_all_games
from payment import add_cc, add_paypal, add_riseup, show_all_payment
from data import vis_data
from users import add_dev, find_dev, add_user, find_user, show_all_users, show_all_devs

CORS(app)

port = 4293
@app.route('/')
def index():
  return "Hello world!"


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


@app.route("/create/user", methods=["POST"])
@cross_origin()
def add_user_endpoint():
  content = request.form
  if not content:
       return "<h1> Error! </h1><p>You need some form content</p>"
  username, password = content.get("username"), content.get("password")
  email, fullname = content.get("email"), content.get("name")
  user_from_db = find_user(username)
  if user_from_db:
       return "<h1> Error! </h1> Your username already has an account!"
  return add_user(username, password, email, fullname)


@app.route("/users")
@cross_origin()
def show_all_users_endpoint():
     return show_all_users()


@app.route("/devs")
@cross_origin()
def show_all_devs_endpoint():
     return show_all_devs()


@app.route("/data")
@cross_origin()
def show_all_data_endpoint():
     return vis_data()


@app.route("/games")
@cross_origin()
def show_all_games_endpoint():
     return show_all_games()


@app.route("/create/game", methods=["POST"])
@cross_origin()
def add_gamelisting_endpoint():
  content = request.form
  if not content:
       return "<h1> status </h1> <p> You need some form content </p>"
  game_name, game_desc, price, category = content.get("title"), content.get("description"), content.get("price"), content.get("category")
  is_on_sale, sale_price = content.get("is_on_sale"), content.get("sale_price")
  if is_on_sale.lower() == 'yes':
       is_on_sale = True
       if not sale_price:
            return "<h1> Error! </h1> <p> You can't have a game on sale without a sale price ... </p>"
  else:
       is_on_sale = False
       sale_price = 0
  developer = content.get("developer")
  developer_from_db = find_dev(developer)
  if not developer_from_db:
       return "<h1> status </h1> <p> The developer you specified doesn't exist! Please create the account. </p>"
  return add_gamelisting(game_name, game_desc, is_on_sale, price, category, sale_price, developer)


@app.route('/create/payment', methods=["POST"])
@cross_origin()
def add_payment_method_endpoint():
  content = request.form
  payment = content.get("payment")
  username, is_primary = content.get("username"), content.get("isprimary")
  is_primary = is_primary == "yes"
  user = find_user(username)
  if not user:
       dev = find_dev(username)
       if not dev:
            return "<h1> Error! </h1> <p> No account found with that username. </p>"
  if not username:
       return "<h1> Error! </h1> <p> You need to specify a username, and let us know if this is your primary method of payment. </p>"
  if not payment:
       return "<h1> Error ! </h1> <p> You need to specify a payment method. </p>"
  if payment == "CreditCard":
       cardnumber, cvc, expirydate = content.get("cardnumber"), content.get("cvc"), content.get("expirydate")
       if not cardnumber or not cvc or not expirydate:
            return "<h1> Error! </h1> <p> You need to specify a card number, CVC and expiry date. </p>"
       return add_cc(username, is_primary, cardnumber, cvc, expirydate)
  elif payment == "Riseup":
       riseup_public_key = content.get('publickey')
       if not riseup_public_key:
            return "<h1> Error! </h1> <p> You need to specify a Riseup Public Key. </p>"
       return add_riseup(username, is_primary, riseup_public_key)
  elif payment == "Paypal":
       ppuser, pppass = content.get("ppusername"), content.get("pppassword")
       if not ppuser or not pppass:
            return "<h1> Error! </h1> <p> You need to specify a Paypal username and password. </p>"
       return add_paypal(username, is_primary, ppuser, pppass)
  else:
       return "<h1> Error! </h1> <p> You need to input a payment type. We support Riseup Wallet, Credit Card and Paypal.</p> "
  return add_payment_method()


@app.route("/paymentmethods")
@cross_origin()
def get_payments():
     username = request.args.get('username')
     if not username:
          return "<h1> Error </h1> <p> You can only view the payment data if you specify the user! </h1>"
     return show_all_payment(username)


if __name__ == '__main__':
  app.run(port=port)
  tunnel.close()
  print("Closed tunnel.")
