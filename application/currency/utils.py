import requests


def get_currency():
    request = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    answer = request.json()['Valute']
    dict_with_currency = {}
    for i in answer.keys():
        dict_with_currency[answer[i]['Name']] = answer[i]['Value']

    return dict_with_currency

