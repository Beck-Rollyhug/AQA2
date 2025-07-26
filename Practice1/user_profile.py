def task2():
    name = input('Привет :) Как тебя зовут? ')
    if not name:
        print('Не увидел имени, попробуй ещё раз')
        return

    job = input('Кем ты работаешь? ')
    if not job:
        print('Не увидел профессию, попробуй ещё раз')
        return

    tool = input('Введите ваш любимый инструмент для тестирования: ')
    if not tool:
        print('Не увидел инструмент, попробуй ещё раз')
        return
    
    print(f'Отлично, {job} {name}, мне тоже нравится {tool} :)')



