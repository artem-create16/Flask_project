from flask import render_template, request, flash

from .form import CurrencyForm
from .utils import get_currency


def show_form():
    form = CurrencyForm()
    result = get_currency()
    if form.validate_on_submit():
        first_selection = request.form.get('select1')
        second_selection = request.form.get('select2')

        print(first_selection)
        print(second_selection)
    else:
        print(form.first_choice.errors)

    return render_template('form_currency.html', html_form=form, option=result)


