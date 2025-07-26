def greet_user(name):
    print(f"Привет, {name}! Добро пожаловать в мир Python!")

def calculate_sum(a, b):
    print('sum: ', a + b)

def task6():
    name = input('Name? ')
    greet_user(name)

    a, b = input('a b: ').split(' ')
    calculate_sum(int(a), int(b))