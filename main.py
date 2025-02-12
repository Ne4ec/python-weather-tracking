import requests

print(40 * '-')
print(10*' ' + "| WEATHER TRACKING |")
print(40 * '-')

def get_result(city):
    server = "https://api.openweathermap.org/data/2.5/weather"
    api_key = "API_KEY" #Replace your API here  

    params = {'q': city, 'appid': api_key, 'units': 'metric', 'lang': 'en'}
    response = requests.get(server, params=params)
    
    if response.status_code == 200:
        weather_data = response.json() #we put all information into one variable
        print("\n")

        print(f"Selected City: {weather_data['name']}")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
    else:
        print(f"Error: {response.status_code} - {response.json().get('message', 'Unknown error')}")


selected_city = input("Which city would you like to get weather info for?\n")
get_result(selected_city)
