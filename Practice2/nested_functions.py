def get_numbers():
    a, b = input('a b: ').split(' ')
    return int(a), int(b)

def get_action():
    return input('action: ')

def calculator():
    a, b = get_numbers()
    action = get_action()
    result = 0

    match action:
        case '+':
            result = a + b
        case '-':
            result = a - b
        case '*':
            result = a * b
        case '/':
            result = a / b
        case _:
            print('Нельзя прочитать операцию')
            return
    
    print('Результат ', result)

def task10():
    calculator()