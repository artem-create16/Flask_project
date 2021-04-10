from flask import Blueprint

from .controller import (show_form, controller_forecast_route,
                         controller_show_currently_route)

weather_blueprint = Blueprint('weather', __name__, template_folder='templates')


@weather_blueprint.route('/', methods=['POST', 'GET'])
def greeting():
    return show_form()


@weather_blueprint.route('/forecast/<city>')
def show_forecast(city):
    return controller_forecast_route(city)


@weather_blueprint.route('/weather/<city>')
def show_currently_weather(city):
    return controller_show_currently_route(city)
