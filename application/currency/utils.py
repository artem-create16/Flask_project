import requests


def return_all_currency():
    request = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    answer = request.json()['Valute']
    dict_with_currency = {}
    for i in answer.keys():
        dict_with_currency[answer[i]['Name']] = answer[i]['Value']
    return dict_with_currency


def get_currency(choice1, choice2):
    request = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    answer = request.json()['Valute']
    dict_with_currency = {}
    for i in answer.keys():
        dict_with_currency[answer[i]['Name']] = answer[i]['Value']
    return dict_with_currency[choice1], dict_with_currency[choice2]
