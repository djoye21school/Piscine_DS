import sys


def create_letter(email):
    name = email.split('@')[0].split('.')[0].capitalize()
    return f'Dear {name}, welcome to our team. We are sure that it will be a pleasure to work ' + \
    'with you. Our company hires only that kind of professionals.'


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(create_letter(sys.argv[1]))
