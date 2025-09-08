import requests

city = 'Hồ Chí Minh'
url = f"https://wttr.in/{city}?format=j1"  # j1 = JSON format
response = requests.get(url)
data = response.json()

# Trích xuất một số thông tin cơ bản
current = data['current_condition'][0]
print("Temperature:", current['temp_C'], "°C")
print("Humidity:", current['humidity'], "%")
print("Weather:", current['weatherDesc'][0]['value'])
print("Wind:", current['windspeedKmph'], "km/h")
