def create_letter(f_name):
    text = f'Dear {f_name}, welcome to our team. ' + \
           'We are sure that it will be a pleasure to work with you. ' + \
           'Our company hires only that kind of professionals.'
    return text


if __name__ == '__main__':
    with open('employees.tsv') as file:
        for i in file.readlines():
            name = i.split('\t')[0]
            if name != 'Name':
                print(create_letter(name))
