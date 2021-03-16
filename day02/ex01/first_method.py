class Research:
    def __init__(self, f_name):
        self.f_name = f_name

    def file_greader(self):
        with open(self.f_name) as file:
            return file.read()


if __name__ == '__main__':
    print(Research('./data.csv').file_greader())
