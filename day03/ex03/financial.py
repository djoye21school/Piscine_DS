import sys
from bs4 import BeautifulSoup
import requests
import time


def get_row(table):
    soup = BeautifulSoup(str(table), "lxml")
    div_list = soup.find_all("div", {"data-test": "fin-col"})
    return [i.text for i in div_list]


def get_title(table):
    soup = BeautifulSoup(str(table), "lxml")
    title_list = soup.find_all("span", {"class": "Va(m)"})
    return [i.text for i in title_list]


def get_table(ticker, parameter):
    url = f'https://finance.yahoo.com/quote/{ticker}/financials?p= {ticker}'
    data = requests.get(url).text
    time.sleep(5)
    soup = BeautifulSoup(data, "lxml")
    rows = soup.find_all("div", {"data-test": "fin-row"})
    titles = get_title(rows)
    if len(titles) == 0:
        raise Exception(f'{ticker} not found')
    if parameter in titles:
        idx = titles.index(parameter)
        return tuple([parameter] + get_row(rows[idx]))
    raise Exception(f'{parameter} not found')


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(get_table(sys.argv[1].upper(), sys.argv[2]))
    else:
        raise Exception('requested field does not exist')
