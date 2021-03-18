import sys
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd


def get_info(ticker, parameter):
    url = f'https://finance.yahoo.com/quote/{ticker}/financials?p= {ticker}'
    data = requests.get(url).text
    soup = BeautifulSoup(data, "lxml")
    table = soup.find_all("div", {"data-test": "fin-row"})
    result = []
    soup = BeautifulSoup(str(table[0]), "lxml")
    div_list = soup.find_all("div", {"data-test": "fin-col"})
    titles = div_list = soup.find_all("div", {"data-test": "fin-col"})
    return div_list
    for div in div_list:
        #if parameter in row:
        if 'title' in div:
            print(div['title'])
        #print(div)
    return
    return result
    return table[0]['title']
    return table[-1]
    '''
    return result
    subdata = BeautifulSoup(table, "lxml")
    #columns = soup.find_all("div", {"data-test": "fin-col"})
    columns = soup.find_all("span")

    return columns
    return table[0]
    #return soup
    '''
    df = pd.read_html(str(table), header=0)[0]
    return df


if __name__ == '__main__':
    if len(sys.argv) == 3:
        print(get_info(sys.argv[1].upper(), sys.argv[2]))
    else:
        raise Exception('requested field does not exist')
