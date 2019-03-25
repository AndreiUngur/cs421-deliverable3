from utils import db

def get_games():
    pass

def add_gamelisting(game_name, game_desc, is_on_sale, price, category, sale_price, developer):
    add_gamelisting_command = 'INSERT INTO GameListing ("title", "description", "is_on_sale", "price", "category", "sale_price", "developer_username")' \
                              f"VALUES ('{game_name}', '{game_desc}', {is_on_sale}, {price}, '{category}', {sale_price}, '{developer}');"
    try:
      db.engine.execute(add_gamelisting_command)
    except Exception as e:
        return {"error": str(e)}
    return {"status": "success"}


