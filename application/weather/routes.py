from flask import Blueprint, render_template

from .controller import (show_form, controller_forecast_route,
                         controller_show_currently_route)

weather_blueprint = Blueprint('weather', __name__, template_folder='templates')


@weather_blueprint.route('/weather', methods=['POST', 'GET'])
def greeting():
    return show_form()


@weather_blueprint.route('/weather/forecast/<city>')
def show_forecast(city):
    return controller_forecast_route(city)


@weather_blueprint.route('/weather/<city>')
def show_currently_weather(city):
    return controller_show_currently_route(city)


@weather_blueprint.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
