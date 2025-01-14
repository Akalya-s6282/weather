import requests
city =input ( "enter the city: ")





api_key = "5cf9ab1afaee86eab7f55f71200c157c"
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
weather= requests.get(url)
print(weather.status_code)

data = weather.json()
weather_data = {
 'city': data['name'],
  'temperature': data['main']['temp'],
  'description': data['weather'][0]['description'],
   'icon': data['weather'][0]['icon']
}                                            

print(f"City: {weather_data['city']}")
print(f"Temperature: {weather_data['temperature']}°C")
print(f"Description: {weather_data['description']}")
print(f"Icon Code: {weather_data['icon']}")