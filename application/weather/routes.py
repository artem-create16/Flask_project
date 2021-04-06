from flask import Blueprint

from .controller import (show_form, show_weather_for_show_forecast_route,
                         show_weather_for_show_currently_route)

weather_blueprint = Blueprint('weather', __name__, template_folder='templates')


@weather_blueprint.route('/', methods=['POST', 'GET'])
def greeting():
    return show_form()


@weather_blueprint.route('/forecast/<city>')
def show_forecast(city):
    return show_weather_for_show_forecast_route(city)


@weather_blueprint.route('/weather/<city>')
def show_currently_weather(city):
    return show_weather_for_show_currently_route(city)
