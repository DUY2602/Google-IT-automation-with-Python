import requests

city = input("Enter your city: ").strip()

print("\n--- Function Menu ---")
print("1️⃣  Current weather")
print("2️⃣  3-day forecast")

choice = input("Choose an option (1 or 2): ").strip()

url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)
data = response.json()

if choice == "1":
    current = data['current_condition'][0]
    print(f"\n🌡️ Temperature: {current['temp_C']}°C")
    print(f"💧 Humidity: {current['humidity']}%")
    print(f"☀️ Weather: {current['weatherDesc'][0]['value']}")
    print(f"🌬️ Wind: {current['windspeedKmph']} km/h")
elif choice == "2":
    forecast = data['weather'][:3]  # 3-day forecast
    for day in forecast:
        date = day['date']
        avgtemp = day['avgtempC']
        maxtemp = day['maxtempC']
        mintemp = day['mintempC']
        desc = day['hourly'][4]['weatherDesc'][0]['value']  # approx midday
        print(f"\n📅 Date: {date}")
        print(f"🌡️ Avg Temp: {avgtemp}°C (Min: {mintemp}°C, Max: {maxtemp}°C)")
        print(f"☀️ Weather: {desc}")
else:
    print("❌ Invalid choice!")