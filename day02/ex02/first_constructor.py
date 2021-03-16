import sys
import os


class Research:
    def __init__(self, f_name):
        self.f_name = f_name

    def file_greader(self):
        with open(self.f_name) as file:
            text = file.readlines()
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
        return ''.join(text)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(Research(sys.argv[1]).file_greader())
