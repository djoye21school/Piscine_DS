def data_types():
    # int, str, float, bool, list, dict, tuple, set]
    var = [0, '', 0.0, False, list(), {}, (0, 0), set()]
    print('[', ', '.join([type(i).__name__ for i in var]), ']', sep='')


if __name__ == '__main__':
    data_types()
