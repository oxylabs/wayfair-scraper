import requests
from pprint import pprint


# Structure payload.
payload = {
    'source': 'wayfair_search',
    'query': 'sofa',
    'start_page': 2,
    'pages': 4
}


# Get response.
response = requests.request(
    'POST',
    'https://realtime.oxylabs.io/v1/queries',
    auth=('user', 'pass1'),
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())