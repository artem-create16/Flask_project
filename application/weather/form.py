from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class FormWeather(FlaskForm):
    city = StringField('City', validators=[DataRequired()])
    forecast = BooleanField('6 days forecast', default=False)
    submit = SubmitField('Show')
