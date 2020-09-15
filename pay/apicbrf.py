import datetime
from logging import getLogger
from collections import namedtuple
import xmltodict
import requests


logger = getLogger(__name__)


Rate = namedtuple('Rate', 'name,rate')


def str_to_float(item: str):
    item = item.replace(',', '.')
    return float(item)


def get_rates(section_id):
    get_curl = "http://www.cbr.ru/scripts/XML_daily.asp"
    date_format = "%d/%m/%Y"

    today = datetime.datetime.today()
    params = {
        "date_req": today.strftime(date_format),
    }
    r = requests.get(get_curl, params=params)
    resp = r.text

    data = xmltodict.parse(resp)

    for item in data['ValCurs']['Valute']:
        if item['@ID'] == section_id:
            r = Rate(
                name=item['CharCode'],
                rate=str_to_float(item['Value']),
            )
            return r
    return None


def main():
    r = get_rates()


if __name__ == '__main__':
    main()




