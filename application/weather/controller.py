from flask import render_template, redirect, url_for
from .utils import get_currently_weather, get_weather_forecast
from .form import FormWeather


def show_form():
    form = FormWeather()

    if form.validate_on_submit():
        city = str(form.city.data)

        if form.forecast.data:
            return redirect(url_for('weather.show_forecast', city=city))

        return redirect(url_for('weather.show_currently_weather', city=city))

    return render_template('form.html', html_form=form)


def controller_forecast_route(city):
    result = get_weather_forecast(city)
    return render_template('forecast.html', town=city, result=result)


def controller_show_currently_route(city):
    result = get_currently_weather(city)
    return render_template('weather.html', town=city, result=result)
