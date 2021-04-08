from flask import render_template

from .form import CurrencyForm
from .utils import get_currency


def show_form():
    form = CurrencyForm()
    result = get_currency()
    if form.validate_on_submit():
        choice = str(form.first_choice.data)
        print(choice)

    return render_template('form_currency.html', html_form=form, option=result)


