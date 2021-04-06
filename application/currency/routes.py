from flask import Blueprint

from .controller import show_form

currency_blueprint = Blueprint('currency', __name__, template_folder='templates')


@currency_blueprint.route('/scam', methods=['POST', 'GET'])
def scam():
    return show_form()

