from flask import Blueprint

from .controller import show_form, controller_show_currency
currency_blueprint = Blueprint('currency', __name__, template_folder='templates')


@currency_blueprint.route('/currency', methods=['POST', 'GET'])
def currency_main():
    return show_form()


@currency_blueprint.route('/currency/show/<choice1>/<choice2>')
def show_currency(choice1, choice2):
    return controller_show_currency(choice1, choice2)
