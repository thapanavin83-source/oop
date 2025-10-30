import requests

city = input("Enter municipality name: ")
api_key = "YOUR_API_KEY"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

print("Weather:", data["weather"][0]["description"])
print("Temperature:", data["main"]["temp"], "Celsius")