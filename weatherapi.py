import requests
# 1. Configuration
# Sign up at openweathermap.org to get your free key!
API_KEY = "Your_API_Key"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
def get_weather(city_name):
    # 2. Build the URL
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"
    try:
        # 3. Fetch Data
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # 4. Parse JSON (Extract specific details)
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            print(f"Weather in {city_name.capitalize()}:")
            print(f"Temperature: {temp}C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {description.capitalize()}")
        else:
            print("City not found. Please check spelling.")
    except Exception as e:
        print(f"Error: {e}")
# 5. Loop (Ask user again and again)
print("Python Weather App Started!")
while True:
    city = input("Enter city name (or 'q' to quit): ")
    if city.lower() == 'q':
        break
    get_weather(city)


