from flask import render_template

from flask import Blueprint


currency_blueprint = Blueprint('currency', __name__, template_folder='templates')


@currency_blueprint.route('/scam', methods=['POST', 'GET'])
def scam():
    list_ = ['Чебурашка', 'Крокодил', 'Мышь']
    return render_template('form_currency.html', option=list_)
