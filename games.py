from utils import db

def get_games():
    pass

def add_gamelisting():
    add_gamelisting = 'INSERT INTO GameListing ("title", "description", "is_on_sale", "price", "category", "sale_price", "developer_username")' \
                      "VALUES ('Poutine Simulator', 'Simulates being a poutine.', false, 69.99, 'Food', 59.99, 'potatodev');"
    db.engine.execute(add_gamelisting)
    return {"status": "success"}

