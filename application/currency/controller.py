from flask import render_template

from .form import CurrencyForm
from .utils import get_the_current_value_of_the_currency


def show_form():
    form = CurrencyForm()
    result = get_the_current_value_of_the_currency()
    return render_template('form_currency.html', html_form=form, option=result)


