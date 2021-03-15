import sys


def stock_prices(ticker):
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

    if ticker in tickers:
        return f'{tickers[ticker]} {stocks[ticker]}'
    return 'Unknown ticker'


if __name__ == '__main__':
    if len(sys.argv) == 2:
        tick = sys.argv[1].upper()
        print(stock_prices(tick))
