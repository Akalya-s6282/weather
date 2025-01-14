from flask import Flask,render_template,request
import requests
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        print(city)
        api_key = "5cf9ab1afaee86eab7f55f71200c157c"
        url =f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response=requests.get(url)
        if response.status_code == 200:
            data = response.json
            weather_data ={'city':data['name'],
                           'temperature': data['main']['temp'],
                           'description': data['weather'][0]['description'],
                           'icon': data['weather'][0]['icon'],

                         }
            print(weater_data)
        else:
            weather_data = {'error': 'City not found!'}
    
    return render_template('index.html', weather=weather_data)

if __name__ == '_main_':
    app.run(debug=True)
