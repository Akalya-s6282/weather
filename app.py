from flask import Flask, render_template, request 
import requests
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    weather_data = {'initial':'Enter the city'}
    print("Initial",weather_data)
    city = request.form.get("city")
    print("city: ",city)
    api_key = "5cf9ab1afaee86eab7f55f71200c157c"
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    weather= requests.get(url)
    print("city =",city)
    print("Code: ",weather.status_code)
    if weather.status_code == 200:
        data = weather.json()
        weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'icon': data['weather'][0]['icon']
        } 
    else: 
        weather_data = {'error':'city not found!'}
    print(weather_data)                                  
    return render_template("index.html",weather=weather_data)

if __name__ == "__main__":
        app.run(debug=True)