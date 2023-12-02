import requests

# API Endpoint URL
api_url = "http://localhost:8000/predict"

# Request Headers (if required)
headers = {
    "Content-Type": "application/json",
}

# Request Body (JSON payload)
payload = {
    "features": [3, 2, 1500, 2, 0, 1, 7, 1200, 300, 2000, 2015, 47.6, 1600]
}

# Make the API Request
try:
    response = requests.post(api_url, json=payload, headers=headers)

    # Check for successful response (status code 200)
    if response.status_code == 200:
        result = response.json()
        print("API Response:", result)
    else:
        print("Error:", response.status_code, response.text)

except requests.exceptions.RequestException as e:
    print("Request Error:", e)
