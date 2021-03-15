import sys

def get_info(file):
    with open(file) as inp:
        with open('employees.tsv', 'w') as out:
            out.write('Name\tSurname\tE-mail\n')
            for i in inp.readlines():
                tmp, mail = i.split('@')
                name, surname = tmp.split('.')
                out.write(f'{name.capitalize()}\t{surname.capitalize()}\t{i.strip()}\n')



if __name__ == '__main__':
    if len(sys.argv) == 2:
        get_info(sys.argv[1])