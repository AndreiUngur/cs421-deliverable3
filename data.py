import datetime
import collections
from utils import db


def vis_data():
    return "Visualizing Data" + vis_reviews() + vis_users()

def vis_reviews():
    HTML_output = '<head><title>Devs</title><link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">' \
                    '</head><body><h1>All Devs</h1>' \
                    '<table><tr><th>Rating</th><th>Date</th>'


    review_data = get_review_data() 

    for d in review_data:
        HTML_output += f"<tr><td>{d[0]}</td><td>{d[1]}</td>"

    HTML_output += "</body>"
    return HTML_output

def vis_users():
    return ""


def get_review_data():
    find_review_data_command = "SELECT rating, date FROM reviews;"
    results = db.engine.execute(find_review_data_command)

    date_map = {} # date -> [rating_sum, count] where date is YEAR-MONTH (ex. "2019-01")
    for row in results:
        rating, date = row
        date = date.isoformat()[:7] # we only care about year and month

        if date not in date_map:
            date_map[date] = [0,0]

        date_map[date][0] += rating
        date_map[date][1] += 1

    review_data = []
    for date in sorted(date_map):
        review_data.append([date, date_map[date][0] / date_map[date][1]])

    return review_data
