import requests
import urllib, json
from datetime import timedelta, date
import sqlite3
from auth import authentication

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

# generic fetch function -> returns json response
def period_fetch(user_id, user_token, json_extension, date, period):
    user_header = {
        'accept': 'application/json',
        'Authorization': 'Bearer ' + user_token,
    }

    # test: grabs today's weight
    # json_extension should be something like '/body/log/weight/date/'
    response = requests.get('https://api.fitbit.com/1/user/' + user_id + json_extension + str(date) + period + '.json', headers=user_header)

    return response

# reformat sleep data
def sleep(user_id, user_token, date):
    response = generic_fetch(user_id, user_token, '/sleep/date/', date)
    print("sleep:")
    print(response)
    values = json.loads(response.content)
    print(values)
    
def temp(user_id, user_token, date):
    response = generic_fetch(user_id, user_token, '/temp/skin/date/', date)
    print("skintemp:")
    print(response)
    #values = json.loads(response.content)
    #print(values)

def cardio(user_id, user_token, date):
    response = generic_fetch(user_id, user_token, '/spo2/date/', date)
    print("spo2:")
    print(response)
    response = generic_fetch(user_id, user_token, '/hrv/date/', date)
    print("hrv:")
    values2 = json.loads(response.content)
    print(values2)
    response = generic_fetch(user_id, user_token, '/cardioscore/date/', date)
    print("vo2:")
    print(response)
    response = generic_fetch(user_id, user_token, '/ecg/list', date)
    print("ecg:")
    print(response)

def breathrate(user_id, user_token, date):
    response = generic_fetch(user_id, user_token, '/br/date/', date)
    print("breathing rate summary:")
    print(response)

def activityzone(user_id, user_token, date):
    response = period_fetch(user_id, user_token, '/activities/active-zone-minutes/date/', date, '1d')
    print("az summary:")
    print(response)
    response = generic_fetch(user_id, user_token, '/activities/date/', date)
    print("activity summary:")
    print(response)

mom_token = authentication('C2R3WZ')
for i in range(1,2): # fetch data for the week
    # make daily entry in dailyTable
    print(sleep('C2R3WZ', mom_token, date.today() - timedelta(i)))
    print(cardio('C2R3WZ', mom_token, date.today() - timedelta(i)))
    print(breathrate('C2R3WZ', mom_token, date.today() - timedelta(i)))
    print(activityzone('C2R3WZ', mom_token, date.today() - timedelta(i)))
    print(temp('C2R3WZ', mom_token, date.today() - timedelta(i)))