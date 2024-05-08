import requests
import urllib, json
from datetime import date

def authentication(user_id):
    # Open the file in read mode
    with open('./auth_management_token.txt', 'r') as file:
        # Read the entire file contents
        manager_token = file.read()

    manager_header = {
        'Authorization': 'Bearer ' + manager_token,
    }

    manager = requests.get('https://dev-pto2334xhilnitn0.us.auth0.com/api/v2/users/fitbit|' + user_id, headers=manager_header)
    values = json.loads(manager.content)

    user_token = values.get('identities')[0].get('access_token')
    return user_token