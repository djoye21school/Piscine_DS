import timeit
import sys
from functools import reduce


def test_loop(n):
    res = 0
    for i in range(1, int(n)+1):
        res += i**2
    return res


def test_reduce(n):
    arr = [i for i in range(1, int(n)+1)]
    return reduce(lambda x, y: x + y**2, arr)


if __name__ == '__main__':
    func = {'loop': 'test_loop', 'reduce': 'test_reduce'}
    if len(sys.argv) != 4:
        exit()
    try:
        f = sys.argv[1]
        if f in func:
            num = int(sys.argv[3])
            print(timeit.timeit(func[f] + f'({num})',
                                number=int(sys.argv[2]),
                                setup="from __main__ import " + func[f]))
        else:
            print('Unsupported operation')
    except ValueError:
        print('The second and third argument must be an integer')
    #  print(test_loop(num))
    #  print(test_reduce(num))
