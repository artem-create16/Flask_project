import requests


def return_currency(*args):
    link = 'https://www.cbr-xml-daily.ru/daily_json.js'
    request = requests.get(link)
    answer = request.json()['Valute']
    dict_with_currency = {}
    for currency in answer:
        dict_with_currency[answer[currency]['Name']] = answer[currency]['Value']
    if args:
        list_with_chosen_currency = [dict_with_currency[choice] for choice in args]
        return list_with_chosen_currency
    else:
        return dict_with_currency

