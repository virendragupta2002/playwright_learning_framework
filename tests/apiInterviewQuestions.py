# Write Python code to:
# · Call API: GET /api/users
# · Print response JSON
# · Handle basic error (status code check)
# Assume response: ["Amit", "Rahul"]

import requests

response = requests.get("https://demo.playwright.dev/api-mocking/api/v1/fruits", timeout=5)

if response.status_code != 200:
    print(f"Response failed with {response.status_code}")
else:
    data = response.json()
    print(data)

for name in data:
    print(name)