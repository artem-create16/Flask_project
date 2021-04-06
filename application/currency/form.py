from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CurrencyForm(FlaskForm):
    first_choice = StringField('Exchange from', validators=[DataRequired()])
    second_choice = StringField('to', validators=[DataRequired()])
    submit = SubmitField('Show')
