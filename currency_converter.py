import urllib2
from urllib import urlopen
import json

URL = 'http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s={from_curr}{to_curr}=X'
YAHOO_CURRENCY_CONVERTER = 'http://finance.yahoo.com/connection/currency-converter-cache?date='


def _get_data(url):
    request = urllib2.Request(url, None, {'Accept-encoding': '*'})
    try:
        response = urllib2.urlopen(request)
    except urllib2.URLError:
        return None
    result = response.read()
    return result


def convert(from_curr, to_curr='USD', amount=1.0, date=None):

    if from_curr.lower() == to_curr.lower():
            return amount

    if not date:

        data = _get_data(URL.format(from_curr=from_curr, to_curr=to_curr))

        if data:
            exchange = data.split(',')
            try:
                converted_amount = u'{0:.3f}'.format(round(float(exchange[1]) * amount, 3))
                return float(converted_amount)

            except (IndexError, ValueError):
                pass

        return 0

    else:
        string_cur = ('[' + "".join(urlopen(YAHOO_CURRENCY_CONVERTER + date).readlines()[8:-5]).replace("\n", "") + ']')
        currencies = json.loads(string_cur)

        if currencies:
            try:
                from_curr_rate = 1
                to_curr_rate = 0

                if from_curr.upper() != 'USD':
                    for cur in currencies:
                        if cur['resource']['fields']['symbol'] == from_curr.upper() + '=X':
                            rate = cur['resource']['fields']
                            from_curr_rate = float(rate['price'])
                            break

                for cur in currencies:
                    if cur['resource']['fields']['symbol'] == to_curr.upper() + '=X':
                        rate = cur['resource']['fields']
                        to_curr_rate = float(rate['price'])
                        break

                return (to_curr_rate/from_curr_rate)*amount

            except Exception as exc:
                print exc
                pass

        return 0
