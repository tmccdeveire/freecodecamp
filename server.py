from flask import Flask, render_template, request
from weather import getCurrentWeather
from waitress import serve

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')
def getWeather():
    city = request.args.get('city')
    weather_data = getCurrentWeather(city)

    if weather_data['cod'] == "404":
        code = weather_data['cod']
        message = weather_data['message']
        # submission = request.args.get('city')
        # submission = city

        print(
            f"\n\n ********* Error {code} :\nMessage: {message} ********* \n\n")

        return render_template(
            "error.html",
            code=weather_data['cod'],
            message=weather_data['message'],
            submission=city
        )

    else:

        return render_template(
            "weather.html",
            title=weather_data['name'].title(),
            status=weather_data['weather'][0]['description'],
            temp=f"{weather_data['main']['temp']:.1f}",
            temp_min=f"{weather_data['main']['temp_min']:.1f}",
            temp_max=f"{weather_data['main']['temp_max']:.1f}",
            feels_like=f"{weather_data['main']['feels_like']:.1f}"
        )


# @app.route('/error')
# def getWeather():
#     city = request.args.get('city')
#     weather_data = getCurrentWeather(city)
#     return render_template(
#         "error.html",
#         submission=request.args.get('city')
#     )


# tells it to run on localhost:8000
if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)
