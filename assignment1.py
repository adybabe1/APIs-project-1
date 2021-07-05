import requests
import spoti.py

CLIENT_ID = '2bb42de1567b4af39721af65662a3c4d'
CLIENT_SECRET = '70285ec23bd943b8b79421cd1ad274c5'

AUTH_URL = 'https://accounts.spotify.com/api/token'
# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

print(auth_response.status_code)

auth_response_data = auth_response.json()

auth_response_data

access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

BASE_URL = 'https://api.spotify.com/v1/'

track_id = '6mFkJmJqdDVQ1REhVfGgd1'

r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

r = r.json()