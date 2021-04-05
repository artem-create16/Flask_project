from flask import Blueprint

from application import app
from .controller import (show_form, show_weather_for_show_forecast_rout,
                         show_weather_for_show_currently_rout)

weather_blueprint = Blueprint('weather', __name__, template_folder='templates')


@app.route('/', methods=['POST', 'GET'])
def greeting():
    return show_form()


@app.route('/forecast/<city>')
def show_forecast(city):
    return show_weather_for_show_forecast_rout(city)


@app.route('/weather/<city>')
def show_currently_weather(city):
    return show_weather_for_show_currently_rout(city)
