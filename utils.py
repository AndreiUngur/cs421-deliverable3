import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from sshtunnel import SSHTunnelForwarder


"""
Utils related to the app setup
"""
# app initialization
app = Flask(__name__)
app.debug = True


# Config
db_username = os.environ.get("PSQL_USER", "")
db_pw = os.environ.get("PSQL_PW", "")
db_name = os.environ.get("PSQL_DB", "")

ssh_server = os.environ.get("SSH_SERVER", "")
ssh_username = os.environ.get("SSH_USER", "")
ssh_password = os.environ.get("SSH_PW", "")

try:
  tunnel = SSHTunnelForwarder((ssh_server, 22),
                              ssh_username=ssh_username,
                              ssh_password=ssh_password,
                              remote_bind_address=('localhost', 5432))
  tunnel.start()
  db_uri = f'postgresql://{db_username}:{db_pw}@localhost:{tunnel.local_bind_port}/{db_name}'
  app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
  app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  
  print("server connected")
  print(tunnel.local_bind_port)
  
  db = SQLAlchemy(app)
  find_all_gamelistings_command = "SELECT * FROM GameListing;"
  results = db.engine.execute(find_all_gamelistings_command)
  print(results.first())
except:
  print("Connection Failed")


# db_uri = f'postgresql://{db_username}:{db_pw}@localhost/{db_name}'
# app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# print("server connected")
# db = SQLAlchemy(app)