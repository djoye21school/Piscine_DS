def data_types():
    var = [0, '', 0.0, False, [], {'a':'b'}, (0, 0), {'a', 'b'}]
    print('[', ', '.join([type(i).__name__ for i in var]), ']', sep='')


if __name__ == '__main__':
    data_types()
