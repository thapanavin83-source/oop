import requests

try:
    response = requests.get("https://api.chucknorris.io/jokes/random")
    if response.status_code == 200:
        print(response.json()["value"])
    else:
        print("Failed to fetch joke, status code:", response.status_code)
except Exception as e:
    print("Error:", e)