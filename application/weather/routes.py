from flask import render_template, redirect, url_for

from application import app
from .utils.show_weather import get_currently_weather, get_weather_forecast
from .form import FormWeather


@app.route('/', methods=['POST', 'GET'])
def greeting():
    form = FormWeather()
    try:
        if form.validate_on_submit():
            city = str(form.city.data)
            if form.forecast.data == True:
                return redirect(url_for('show_forecast', city=city))
            return redirect(url_for('show_currently_weather', city=city))

    except Exception as e:
        print(str(e))
    return render_template('weather/templates/form.html', html_form=form)


@app.route('/forecast/<city>')
def show_forecast(city):
    result = get_weather_forecast(city)
    return render_template('weather/templates/forecast.html', town=city, result=result)


@app.route('/weather/<city>')
def show_currently_weather(city):
    result = get_currently_weather(city)
    return render_template('weather.html', town=city, result=result)