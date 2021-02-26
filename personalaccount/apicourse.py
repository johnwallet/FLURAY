from logging import getLogger
from collections import namedtuple
import xmltodict
import requests


logger = getLogger(__name__)


Rate = namedtuple('Rate', 'name,rate')


def get_rates():
    get_curl = "http://www.floatrates.com/daily/usd.xml"

    r = requests.get(get_curl)
    resp = r.text

    data = xmltodict.parse(resp)

    return data

def main():
    r = get_rates()


if __name__ == '__main__':
    main()
