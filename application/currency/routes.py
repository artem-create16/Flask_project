from flask import Blueprint

from .controller import show_form

currency_blueprint = Blueprint('currency', __name__, template_folder='templates')


@currency_blueprint.route('/currency', methods=['POST', 'GET'])
def currency_main():
    return show_form()

