cat main.py 
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

        # output: works like a dictionaries
        print(f"Selected City: {weather_data['name']}")
        print(f"Weather: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
    if response.status_code < 250:
        print("The Server is not working now, try later")


selected_city = input("Which city would you like to get weather info for?\n")

print(get_result(selected_city))
