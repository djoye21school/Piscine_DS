import os
from random import randint


class Research:
    def __init__(self, f_name):
        self.f_name = f_name
        self.data = self.file_greader()
        self.calculations = self.Analytics(self.data)

    def file_greader(self, has_header=True):
        with open(self.f_name) as file:
            text = file.readlines()
            body = text
            if has_header:
                header = text[0]
                if len(header.split(',')) != 2:
                    raise Exception("Incorrect header")
                body = text[1:]
            if len(body) == 0:
                raise Exception("The file does not contain any data")
            for i in body:
                count = i.count('1') + i.count('0')
                if len(header.split(',')) != 2 or \
                        len(i.strip()) != 3 or count != 2:
                    raise Exception("Invalid data")
        return [[int(x) for x in i.strip().split(',')] for i in body]

    class Calculations:
        def __init__(self, data):
            self.data = data
            self.count = self.counts()
            self.fraction = self.fractions()

        def counts(self):
            x = [i[0] for i in self.data]
            y = [i[1] for i in self.data]
            return [sum(x), sum(y)]

        def fractions(self):
            return [self.count[0] / len(self.data) * 100,
                    self.count[1] / len(self.data) * 100]

    class Analytics(Calculations):

        def predict_random(self, num):
            dict_res = {0: [0, 1], 1: [1, 0]}
            return [dict_res[randint(0, 1)] for i in range(num)]

        def predict_last(self):
            return self.data[-1]

        def save_file(self, data, file_name, ext='txt'):
            with open(file_name + '.' + ext, 'w') as file:
                file.write(data)
