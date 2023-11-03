### Get QUIP user's info

import requests

# Access token an be obtained here: https://quip-apple.com/dev/token
access_token = 'xyz'

# Define the Quip API endpoint for the user's information
# link may look different for quip corporate users
api_url = 'https://platform.quip.com/1/users/current'

# Set up headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Send a GET request to the API endpoint
response = requests.get(api_url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    user_info = response.json()
    print("User Information:")
    print("Name: ", user_info['name'])
else:
    print(f"Error: {response.status_code} - {response.text}")
