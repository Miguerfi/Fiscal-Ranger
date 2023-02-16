import requests
import json


class CoinsConvApi:
    def get_coins(self, coins):
        response = requests.get("https://economia.awesomeapi.com.br/last/" + coins)
        tojson = json.loads(response.text)
        first_currency = next(iter(tojson))
        resultado = f'''
CONVERSION: {str(coins).upper()}
BASE COIN:{tojson[first_currency]['code']}
COIN IN:{tojson[first_currency]['codein']}
HIGH:{tojson[first_currency]['high']}
LOW:{tojson[first_currency]['low']} 
VARIATION:{tojson[first_currency]['varBid']}
% OF VARIATION:{tojson[first_currency]['pctChange']}
BUY:{tojson[first_currency]['bid']}
SELL:{tojson[first_currency]['ask']}'''
        return resultado 
