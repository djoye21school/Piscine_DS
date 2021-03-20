import timeit
import random
from collections import Counter


def my_counter(r_values):
    dict_count = dict()
    for i in r_values:
        if i in dict_count:
            dict_count[i] += 1
        else:
            dict_count[i] = 1
    return dict_count


def top(r_values):
    dict_count = my_counter(r_values)
    return sorted(dict_count.items(), key=(lambda x: -x[1]))[:10]


def check(r_values):
    dict_count = my_counter(r_values)
    print(dict_count)
    print(top(r_values))
    print(Counter(r_values).most_common(10))


def main():
    r_values = [random.randint(0, 100) for i in range(1000000)]
    # check(r_values)
    num = 1
    print('my function:',
          timeit.timeit(f'my_counter({r_values})', number=num,
                        setup="from __main__ import my_counter"))
    print('Counter:',
          timeit.timeit(f'Counter({r_values})', number=num,
                        setup="from __main__ import Counter"))
    print('my top:',
          timeit.timeit(f'top({r_values})', number=num,
                        setup="from __main__ import top"))
    print('Counter\'s top:',
          timeit.timeit(f'Counter({r_values}).most_common(10)', number=num,
                        setup="from __main__ import Counter"))


if __name__ == '__main__':
    main()
