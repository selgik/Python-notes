import requests

# Access token can be obtained here: https://quip-apple.com/dev/token
access_token = 'xyz123'

document_api_url = 'https://platform.quip.com/1/threads/edit-document'

# Set up headers with the access token for both requests
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Create the payload for the POST request to edit a document
document_payload = {
    "thread_id": "e8EbA5r4CLyb",
    "format": "html",
    "content": "<li>test text</li>",
    "location": 0  # Insert at the beginning of the document
}

# Send a POST request to edit the document
response_document = requests.post(document_api_url, headers=headers, json=document_payload)

# Check if the document edit request was successful
if response_document.status_code == 200:
    print("Document edited successfully.")
else:
    print(f"Error (Document Edit): {response_document.status_code} - {response_document.text}")
