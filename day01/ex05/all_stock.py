import sys


def stock_info(arg):
    companies = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    stocks = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    tickers = {v: k for k, v in companies.items()}
    ticker = arg.upper()
    company = arg.capitalize()
    if ticker in tickers:
        return f'{ticker} is a ticker symbol for {tickers[ticker]}'
    if company in companies:
        return f'{company} stock price is {stocks[companies[company]]}'
    return f'{arg} is an unknown company or an unknown ticker symbol'


def get_info(argv):
    arr = argv.replace(' ', '').split(',')
    if '' in arr:
        return
    for i in arr:
        print(stock_info(i))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_info(sys.argv[1])
