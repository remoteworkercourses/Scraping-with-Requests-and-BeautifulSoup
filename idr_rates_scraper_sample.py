import requests

# json_data = requests.get('http://www.floatrates.com/daily/idr.json')
json_data = {
    "usd": {"code": "USD", "alphaCode": "USD", "numericCode": "840", "name": "U.S. Dollar", "rate": 6.7074033278108e-5,
            "date": "Sun, 13 Sep 2020 12:00:01 GMT", "inverseRate": 14908.899183887},
    "eur": {"code": "EUR", "alphaCode": "EUR", "numericCode": "978", "name": "Euro", "rate": 5.660735562728e-5,
            "date": "Sun, 13 Sep 2020 12:00:01 GMT", "inverseRate": 17665.548742186}}
# print(json_data.json())
for data in json_data.values():
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])
