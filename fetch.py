import requests
import urllib, json
from datetime import date

# Open the file in read mode
with open('./auth_management_token.txt', 'r') as file:
    # Read the entire file contents
    manager_token = file.read()

manager_header = {
    'Authorization': 'Bearer ' + manager_token,
}

manager = requests.get('https://dev-pto2334xhilnitn0.us.auth0.com/api/v2/users/fitbit|C2Z4ZJ', headers=manager_header)
values = json.loads(manager.content)

user_token = values.get('identities')[0].get('access_token')
user_id = values.get('identities')[0].get('user_id')

user_header = {
    'accept': 'application/json',
    'Authorization': 'Bearer ' + user_token,
}

# test: grabs today's weight
today = date.today()
user = requests.get('https://api.fitbit.com/1/user/' + user_id + '/body/log/weight/date/' + str(today) + '.json', headers=user_header)

print(user.content)