from flask import render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from application import app
from show_weather import get_currently_weather
from show_weather import get_weather_forecast


class FormWeather(FlaskForm):
    city = StringField('City', validators=[DataRequired()])
    forecast = BooleanField('6 days forecast', default=False)
    submit = SubmitField('Show')


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
        return (str(e))
    return render_template('form.html', html_form=form)


@app.route('/forecast/<city>')
def show_forecast(city):
    result = get_weather_forecast(city)
    return render_template('forecast.html', town=city, result=result)


@app.route('/weather/<city>')
def show_currently_weather(city):
    result = get_currently_weather(city)
    return render_template('weather.html', town=city, result=result)