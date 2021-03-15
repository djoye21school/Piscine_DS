import sys


def get_clients():
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com', 'john@snow.is',
               'bill_gates@live.com', 'mark@facebook.com', 'elon@paypal.com', 'jessica@gmail.com']
    return set(clients)


def get_participants():
    participants = ['walter@heisenberg.com', 'vasily@mail.ru', 'pinkman@yo.org', 'jessica@gmail.com',
                    'elon@paypal.com', 'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    return set(participants)


def get_recipients():
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']
    return set(recipients)


def call_center():
    return sorted(list(get_clients() - get_recipients()))


def potential_clients():
    return sorted(list(get_participants() - get_clients()))


def loyalty_program():
    return sorted(list(get_clients() - get_participants())) # sorting?


def marketing(task):
    if task == 'call_center':
        return call_center()
    if task == 'potential_clients':
        return potential_clients()
    if task == 'loyalty_program':
        return loyalty_program()
    raise ValueError('invalid command')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        result = marketing(sys.argv[1])
        for i in result:
            print(i)
