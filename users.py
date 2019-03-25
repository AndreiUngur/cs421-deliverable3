from datetime import datetime
from utils import db

def add_dev(username, password, email, studio):
    add_dev_command = 'INSERT INTO DeveloperAccount("username", "password", "email", "creation_date", "studio_name")' \
                      f"VALUES('{username}', '{password}', '{email}', '{datetime.now()}', '{studio}');"
    try:
      print(db.engine.execute(add_dev_command).keys())
    except Exception as e:
        return {"error": str(e)}
    return {"status": "success"}
