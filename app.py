import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index(): 
    if  request.method == 'POST':
        city = request.form['city']
        if city =="":
            error ="Enter city name "
            return render_template('index.html', error=error)
        
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=1bab5ecba89d80a433fae6c22dbe5d98'
        r = requests.get(url.format(city)).json()       #response as city, needed the json output so json()
            
        weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon':  r['weather'][0]['icon'],
        }
        return render_template('index.html',weather=weather)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)