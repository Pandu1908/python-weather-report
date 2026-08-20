import requests

city = input("Enter city name: ")

url = "https://wttr.in/" + city + "?format=j1"

try:
    response = requests.get(url)
    data = response.json()

    current = data["current_condition"][0]

    print("\n--- Weather Report ---")
    print("City:", city)
    print("Temperature:", current["temp_C"], "°C")
    print("Feels Like:", current["FeelsLikeC"], "°C")
    print("Humidity:", current["humidity"], "%")
    print("Wind Speed:", current["windspeedKmph"], "km/h")
    print("Condition:", current["weatherDesc"][0]["value"])

except Exception:
    print("Unable to fetch weather information.")
