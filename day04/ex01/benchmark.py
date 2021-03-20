import timeit


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


def test_map_list():
    emails = get_emails()
    return list(map(lambda x: x if x.endswith('@gmail.com') else None, emails))


def check():
    print(test_loop(), test_lc(), test_map_list(), sep='\n\n')
    print(*test_map())


if __name__ == '__main__':
    num = 90000000
    time_loop = timeit.timeit('test_loop()', number=num,
                              setup="from __main__ import test_loop")
    time_lc = timeit.timeit('test_lc()', number=num,
                            setup="from __main__ import test_lc")
    time_map = timeit.timeit('test_map()', number=num,
                             setup="from __main__ import test_map")
    '''
    time_map_list = timeit.timeit('test_map_list()', number=num,
                                  setup="from __main__ import test_map_list")
    '''
    times = sorted([time_loop, time_lc, time_map])  # , time_map])
    min_time = times[0]
    bench = ''
    if min_time == time_loop:
        bench = 'loop'
    elif min_time == time_lc:
        bench = 'list comprehension'
    elif min_time == time_map:
        bench = 'map'
    '''
    else:
        bench = 'map_list'
    '''
    print('it is better to use a ' + bench)
    print(' vs '.join(map(str, times)))
    # print('map_time: ', time_map, ', map_list_time: ', time_map_list)
    #check()
