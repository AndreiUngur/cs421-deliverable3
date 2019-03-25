from datetime import datetime
from utils import db

HTML_output = '<head>' \
              '<title>Games</title>' \
              '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">' \
              '</head>' \
              '<body>'


def add_cc(username, is_primary, cardnumber, cvc, expirydate):
    add_cc_command = 'INSERT INTO CreditCard ("date_added", "is_primary", "username", "card_number", "cvc", "exp_date")' \
                     f"VALUES ('{datetime.now()}', {is_primary}, '{username}', '{cardnumber}', '{cvc}', '{expirydate}');"
    try:
        db.engine.execute(add_cc_command)
    except Exception as e:
        if "reject_expired_cards" in str(e):
            return "<h1> Error! </h1> <p> Your card is expired ... You can only pay with cards that aren't expired! </p>"
        return f"<h1> Error! </h1> <p> {str(e)}"
    return HTML_output + get_all_cc(username)


def add_paypal(username, is_primary, ppuser, pppass):
    add_paypal_command = 'INSERT INTO PayPal ("date_added", "is_primary", "username", "pp_email", "pp_password")' \
                         f"VALUES ('{datetime.now()}', {is_primary}, '{username}', '{ppuser}', '{pppass}');"
    try:
        db.engine.execute(add_paypal_command)
    except Exception as e:
        return f"<h1> Error! </h1> <p> {str(e)}"
    return HTML_output + get_all_paypal(username)


def add_riseup(username, is_primary, riseup_public_key):
    add_riseup_command = 'INSERT INTO RiseupWallet ("date_added", "is_primary", "username", "public_key")' \
                         f"VALUES ('{datetime.now()}', {is_primary}, '{username}', '{riseup_public_key}');"
    try:
        db.engine.execute(add_riseup_command)
    except Exception as e:
        return f"<h1> Error! </h1> <p> {str(e)}"
    return HTML_output + get_all_riseup(username)


def get_all_cc(username):
    get_cc_command = f"SELECT date_added, username, card_number, cvc, exp_date, is_primary FROM CreditCard WHERE username = '{username}'"
    try:
        results = db.engine.execute(get_cc_command)
    except Exception as e:
        return f"<h1> Error! </h1> <p> {str(e)}"
    HTML = '<h1> Credit Cards </h1> <table class="table"><thead><th>Date Added</th><th>Username</th><th>Card Number</th><th>CVC</th><th>Expiry Date</th><th>Is Primary?</th></thead><tbody>'
    for row in results:
        date_added, username, card_number, cvc, expiry_date, is_primary = row
        HTML += f"<thead><td>{date_added}</td><td>{username}</td><td>{card_number}</td><td>{cvc}</td><td>{expiry_date}</td><td>{is_primary}</td></thead><tbody>"
    return HTML + "</tbody></table>"


def get_all_paypal(username):
    get_paypal_command = f"SELECT date_added, username, pp_email, pp_password, is_primary FROM PayPal WHERE username = '{username}'"
    try:
        results = db.engine.execute(get_paypal_command)
    except Exception as e:
        return f"<h1> Error! </h1> <p> {str(e)}"
    HTML = '<h1> Paypal Accounts </h1><table class="table"><thead><th>Date Added</th><th>Username</th><th>PP Username</th><th>PP Password</th><th>Is Primary?</th></thead><tbody>'
    for row in results:
        date_added, username, pp_user, pp_pass, is_primary = row
        HTML += f"<tr><td>{date_added}</td><td>{username}</td><td>{pp_user}</td><td>{pp_pass}</td><td>{is_primary}</td></tr>"
    return HTML + "</tbody></table>"


def get_all_riseup(username):
    get_riseup_command = f"SELECT date_added, username, public_key, is_primary FROM RiseupWallet WHERE username = '{username}'"
    try:
        results =  db.engine.execute(get_riseup_command)
    except Exception as e:
        return f"<h1> Error! </h1> <p> {str(e)}"
    HTML = '<h1> Riseup Wallets </h1><table class="table"><thead><th>Date Added</th><th>Username</th><th>Public Key</th><th>Is Primary?</th></thead><tbody>'
    for row in results:
        date_added, username, public_key, is_primary = row
        HTML += f"<tr><td>{date_added}</td><td>{username}</td><td>{public_key}</td><td>{is_primary}</td></tr>"
    return HTML + "</tbody></table>"


def show_all_payment(username):
    return HTML_output + get_all_cc(username) + get_all_paypal(username) + get_all_riseup(username)
    