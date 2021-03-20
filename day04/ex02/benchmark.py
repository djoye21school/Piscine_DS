import timeit
import sys


def get_emails():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
              'anna@live.com', 'philipp@gmail.com']
    return emails * 5


def test_loop():
    emails = get_emails()
    arr = []
    for i in emails:
        if i.endswith('@gmail.com'):
            arr.append(i)
    return arr


def test_lc():
    emails = get_emails()
    return [i for i in emails if i.endswith('@gmail.com')]


def test_map():
    emails = get_emails()
    return map(lambda x: x if x.endswith('@gmail.com') else None, emails)


def test_filter():
    emails = get_emails()
    return filter(lambda x: x.endswith('@gmail.com'), emails)


if __name__ == '__main__':
    func = {'loop': 'test_loop',
            'list_comprehension': 'test_lc',
            'map': 'test_map',
            'filter': 'test_filter'}
    if len(sys.argv) != 3:
        exit()
    try:
        f = sys.argv[1]
        if f in func:
            print(timeit.timeit(func[f] + '()', number=int(sys.argv[2]),
                                setup="from __main__ import " + func[f]))
        else:
            print('Unsupported operation')
    except ValueError:
        print('The second argument must be an integer')
