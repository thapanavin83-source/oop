import requests
api = "3d8fa12f757af721ab5ddc99266cc262"

city = input("Enter the city name: ")
url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api}"
try:

    response = requests.get(url)
    data = response.json()
    lat = data[0]["lat"]
    lon = data[0]['lon']
except Exception as e:
    print("Error:", e)

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"
try:

    response = requests.get(url)
    data = response.json()
    degree = data ['main']['temp'] - 272.15
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Temperature: {degree:.2f} Celsius")
except Exception as e:
    print("Error:", e)