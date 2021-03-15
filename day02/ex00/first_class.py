class Must_read:
    def __init__(self, f_name):
        with open(f_name) as file:
            print(file.read())


if __name__ == '__main__':
    Must_read('./data.csv')
