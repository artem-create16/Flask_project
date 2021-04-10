from flask import render_template, request, redirect, url_for

from .form import CurrencyForm
from .utils import return_currency


def show_form():
    form = CurrencyForm()
    result = return_currency()
    choice1 = request.form.get('select1')
    choice2 = request.form.get('select2')
    if choice1 is not None and choice2 is not None:
        return redirect(url_for('currency.show_currency', choice1=choice1, choice2=choice2))

    return render_template('form_currency.html', html_form=form, option=result)


def controller_show_currency(choice1, choice2):
    result = return_currency(choice1, choice2)
    return render_template('show_currency.html', choice1=choice1, choice2=choice2, result=result)



