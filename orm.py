import requests
import urllib, json
from datetime import date
import sqlite3

conn = sqlite3.connect('clairvoyant.db')
cursor = conn.cursor()
# import row into dailyTable automatically on a daily basis.

# generic fetch function -> returns json response
def generic_fetch(user_id, user_token, json_extension, date):
    user_header = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + user_token,
    }

    # test: grabs today's weight
    # json_extension should be something like '/body/log/weight/date/'
    response = requests.get('https://api.fitbit.com/1/user/' + user_id + json_extension + str(date) + '.json', headers=user_header)

    return response

# reformat sleep data
def sleep(user_id, user_token, date):
    response = generic_fetch(user_id, user_token, '/sleep/date/', date)
    values = json.loads(response.content)
    
def temp(user_id, user_token, date):
    response = generic_fetch(user_id, user_token, '/temp/skin/date/', date)
    values = json.loads(response.content)
    print(values)