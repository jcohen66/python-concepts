import requests

# Replace the URL with your server's endpoint
webhook_url = 'http://localhost:8000'

# Define the payload to send to the webhook
payload = {'message': 'Hello from webhook provider!'}

# Send the POST request to the webhook
response = requests.post(webhook_url, json=payload)

# Check the response status code
if response.status_code == 200:
    print("Webhook request sent successfully!")
else:
    print("Failed to send webhook request. Status code:", response.status_code)
