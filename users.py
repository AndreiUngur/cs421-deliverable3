from datetime import datetime
from utils import db

def add_dev(username, password, email, studio):
  add_dev_command = 'INSERT INTO DeveloperAccount("username", "password", "email", "creation_date", "studio_name")' \
                    f"VALUES('{username}', '{password}', '{email}', '{datetime.now()}', '{studio}');"
  try:
    db.engine.execute(add_dev_command)
  except Exception as e:
      if "password_check" in str(e):
          return "<h1> Error </h1> <p> Your password must be at least 6 characters long! Don't let sneaky gamers steal your games. </p>"
      return f"<h1> Error </h1><p> {str(e)} </p>"
  dev = find_dev(username)
  username, password, email, creation_date, studio = dev

  HTML_output = '<head><title>Users</title><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">' \
                f'</head><body><h1>Hello, {username}</h1>' \
                '<table class="table"><thead><th>Password</th><th>Email</th><th>Creation Date</th><th>Studio</th></thead><tbody>'
  HTML_output += f'<tr><td>{password}</td><td>{email}</td><td>{creation_date}</td><td>{studio}</td></tbody></body>'

  return HTML_output


def find_dev(username):
  find_dev_command = f"select * from developeraccount where username='{username}';"
  result = db.engine.execute(find_dev_command).first()
  return result


def show_all_devs():
  find_all_gamelistings_command = "SELECT * FROM DeveloperAccount;"
  results = db.engine.execute(find_all_gamelistings_command)
  HTML_output = '<head><title>Devs</title><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">' \
                '</head><body><h1>All Devs</h1>' \
                '<table class="table"><thead><th>Username</th><th>Password</th><th>Email</th><th>Creation Date</th><th>Studio Name</th></thead><tbody>'

  for row in results:
    username, password, email, creation_date, studio_name = row
    HTML_output += f"<tr><td>{username}</td><td>{password}</td><td>{email}</td><td>{creation_date}</td><td>{studio_name}</td></tr>"
  HTML_output += "</tbody></table></body>"
  return HTML_output


def add_user(username, password, email, fullname):
  add_user_command = 'INSERT INTO UserAccount("username", "password", "email", "creation_date", "name")' \
                    f"VALUES('{username}', '{password}', '{email}', '{datetime.now()}', '{fullname}');"
  try:
    db.engine.execute(add_user_command)
  except Exception as e:
      if "password_check" in str(e):
          return "<h1> Error </h1> <p> Your password must be at least 6 characters long! Don't let sneaky gamers steal your games. </p>"
      return f"<h1> Error </h1><p> {str(e)} </p>"
  user = find_user(username)
  username, password, email, creation_date, name = user

  HTML_output = '<head><title>Users</title><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">' \
                f'</head><body><h1>Hello, {username}</h1>' \
                '<table class="table"><thead><th>Password</th><th>Email</th><th>Creation Date</th><th>Full Name</th></thead>'
  HTML_output += f'<tr><td>{password}</td><td>{email}</td><td>{creation_date}</td><td>{name}</td></tbody></table></body>'

  return HTML_output


def find_user(username):
  find_user_command = f"select * from useraccount where username='{username}';"
  result = db.engine.execute(find_user_command).first()
  return result


def show_all_users():
  find_all_gamelistings_command = "SELECT * FROM UserAccount;"
  results = db.engine.execute(find_all_gamelistings_command)
  HTML_output = '<head><title>Users</title><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">' \
                '</head><body><h1>All Users</h1>' \
                '<table class="table"><thead><th>Username</th><th>Password</th><th>Email</th><th>Creation Date</th><th>Full Name</th></thead><tbody>'

  for row in results:
    username, password, email, creation_date, full_name = row
    HTML_output += f"<tr><td>{username}</td><td>{password}</td><td>{email}</td><td>{creation_date}</td><td>{full_name}</td></tr>"
  HTML_output += "</tbody></table></body>"
  return HTML_output

