import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def get_weather_data(city):
    #made f string to pass city in the url
    url = f'http://api.openweathermap.org/data/2.5/weather?q={ city }&appid=1bab5ecba89d80a433fae6c22dbe5d98'
    #response as city, needed the json output so json()
    r = requests.get(url).json()       
    return r

@app.route('/', methods=['POST', 'GET'])
def index(): 
    if  request.method == 'POST':
        city = request.form['city']
        if city =="":
            error ="Enter city name "
            return render_template('index.html', error=error)
        
        r = get_weather_data(city)
        if r['cod'] == 200:
            weather = {
                'city' : r['name'],
                'temperature' : r['main']['temp'],
                'description' : r['weather'][0]['description'],
                'icon':  r['weather'][0]['icon'],
            }
            print(r)
            return render_template('index.html',weather=weather)
        else:
            error = "There is no city in the world with that name!"
            return render_template('index.html', error=error)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)