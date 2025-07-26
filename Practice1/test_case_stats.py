def task3():
    total = 0

    count = 1
    while count < 8:
        testAmount = int(input(f'Кол-во тестов, выполненных за день №{count}: '))
        if not testAmount:
            print('Не получил количество тестов, попробуй ещё раз')
            return
        count += 1
        total += testAmount
    
    print('Общее количество тестов за неделю', total)
    print('Среднее количество тестов в день', total / 7)

    if (total / 7 > 10): print("Отличная работа!")
    else: print("Попробуйте улучшить результат")