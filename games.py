from utils import db


def add_gamelisting(game_name, game_desc, is_on_sale, price, category, sale_price, developer):
  find_gamelisting_command = f"SELECT * FROM GameListing WHERE title='{game_name}';"
  result = db.engine.execute(find_gamelisting_command).first()
  if result:
    return f"<h1> Error! </h1> <p>Your game already exists! : {result}"
  add_gamelisting_command = 'INSERT INTO GameListing ("title", "description", "is_on_sale", "price", "category", "sale_price", "developer_username")' \
                            f"VALUES ('{game_name}', '{game_desc}', {is_on_sale}, {price}, '{category}', {sale_price}, '{developer}');"
  try:
    db.engine.execute(add_gamelisting_command)
  except Exception as e:
      return f"<h1> Error! </h1> <p> {str(e)}"
    
  find_all_gamelistings_by_category_command = f"SELECT * FROM GameListing where category='{category}';"
  HTML_output = '<head>' \
                '<title>Games</title>' \
                '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">' \
                '</head>' \
                '<body>' \
                f'<h1>{category} Games</h1>'
  results = db.engine.execute(find_all_gamelistings_by_category_command)
  for row in results:
    identifier, title, description, is_on_sale, price, category, sale_price, developer = row
    HTML_output += f'<h2>{title}</h2>' \
                    f'<h3>Description</h3> <p>{description}</p> ' \
                    f'<h3>Category</h3> <p> {category} </p> ' \
                    f'<h3>Details</h3> <ul> ' \
                    f'<li>Price: {price}</li><li>Is this on sale? {is_on_sale}</li><li>Sale Price: {sale_price}</li></ul>'
  HTML_output += "</body>"
  return HTML_output


def show_all_games():
  find_all_gamelistings_command = "SELECT * FROM GameListing;"
  results = db.engine.execute(find_all_gamelistings_command)
  HTML_output = '<head>' \
                '<title>Games</title>' \
                '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">' \
                '</head>' \
                '<body>' \
                '<h1>All Games</h1>'

  for row in results:
    identifier, title, description, is_on_sale, price, category, sale_price, developer = row
    HTML_output += f'<h2>{title}</h2>' \
                    f'<h3>Description</h3> <p>{description}</p> ' \
                    f'<h3>Category</h3> <p> {category} </p> ' \
                    f'<h3>Details</h3> <ul> ' \
                    f'<li>Price: {price}</li><li>Is this on sale? {is_on_sale}</li><li>Sale Price: {sale_price}</li></ul>'
  HTML_output += "</body>"
  return HTML_output

