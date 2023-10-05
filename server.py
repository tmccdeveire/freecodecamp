from flask import Flask, render_template, request
from weather import getCurrentWeather
from waitress import serve
from pprint import pprint

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def getWeather():
    city = request.args.get('city').strip()
    weather_data = getCurrentWeather(city)
    print(f"\n\n ********* Successful Return ********* \n\n")

    pprint(weather_data)

    if weather_data['cod'] == 200:
        return render_template(
            "weather.html",
            title=weather_data['name'].title(),
            status=weather_data['weather'][0]['description'],
            temp=f"{weather_data['main']['temp']:.1f}",
            temp_min=f"{weather_data['main']['temp_min']:.1f}",
            temp_max=f"{weather_data['main']['temp_max']:.1f}",
            feels_like=f"{weather_data['main']['feels_like']:.1f}"
        )

    elif weather_data['cod'] == "404":

        print(
            f"\n\n ********* Error {weather_data['cod']} :\nMessage: {weather_data['message']} ********* \n\n")

        return render_template(
            "error.html",
            code=weather_data['cod'],
            errorMessage=weather_data['message'],
            errorInfo=f"We cannot find the submitted city: '{city}'."
        )
    elif weather_data['cod'] == "400":
        code = weather_data['cod']

        print(
            f"\n\n ********* Error {weather_data['cod']} :\nMessage: {weather_data['message']} ********* \n\n")

        return render_template(
            "error.html",
            code=weather_data['cod'],
            errorMessage=weather_data['message'],
            errorInfo=f"Please enter a city, not blank spaces."
        )

    else:

        print(
            f"\n\n ********* Error ********* \n\n")
        pprint(weather_data)

        return render_template(
            "error.html",
            code=weather_data['cod'],
            errorMessage=weather_data['message'],
            errorInfo=f"Unknown Error."
        )


# tells it to run on localhost:8000
if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
