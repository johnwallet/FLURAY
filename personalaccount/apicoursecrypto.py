# bitcoin, ethereum, ethereum-classic, monero, ripple, dash, bitcoin-cash, litecoin
import json
from logging import getLogger
from collections import namedtuple
import requests
import xmltodict

logger = getLogger(__name__)


Rate = namedtuple('Rate', 'name,rate')


def get_rates_crypto():
    get_curl = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2C%20ethereum%2C%20ethereum-classic%2C%20monero%2C%20ripple%2C%20dash%2C%20bitcoin-cash%2C%20litecoin&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    data = requests.get(get_curl).json()
    return data

def main():
    data = get_rates_crypto()


if __name__ == '__main__':
    main()
