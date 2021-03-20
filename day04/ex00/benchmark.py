import timeit


def test_lc():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
              'anna@live.com', 'philipp@gmail.com'] * 5
    return [i for i in emails if i.endswith('@gmail.com')]


def test_loop():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
              'anna@live.com', 'philipp@gmail.com'] * 5
    arr = []
    for i in emails:
        if i.endswith('@gmail.com'):
            arr.append(i)
    return arr


if __name__ == '__main__':
    time_loop = timeit.timeit('test_loop()',
                              setup="from __main__ import test_loop",
                              number=90000000)
    time_lc = timeit.timeit('test_lc()',
                            setup="from __main__ import test_lc",
                            number=90000000)
    if time_lc < time_loop:
        bench = 'list comprehension'
    else:
        bench = 'loop'
    print('it is better to use a ' + bench)
    time = sorted([time_lc, time_loop])
    print(str(time[0]) + ' vs ' + str(time[1]))
