import requests


def get_currency():
    request = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    answer = request.json()
    dict_with_currency = {}
    valute = answer.get('Valute')
    for i in valute.keys():
        dict_with_currency[valute[i]['Name']] = valute[i]['Value']
    # print(dict_with_currency)
    # for i in dict_with_currency.keys():
    #     print(i)
    return dict_with_currency


# get_the_current_value_of_the_currency()