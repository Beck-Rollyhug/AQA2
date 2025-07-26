
def task1():
    name = input('Привет :) Как тебя зовут? ')
    job = input('Кем ты работаешь? ')

    isQA = job.lower() in ['qa', 'aqa', 'tester', 'куа', 'акуа', 'тестер', 'тестировщик']

    if isQA:
        answer = input(f'Если ты, {name}, считаешь себя {job}, то скажи \nЧто такое переменная? ')

        corrects = ['объект', 'запоминает', 'значение', 'памяти']

        words = answer.split(' ')
        mark = len(set(words).intersection(corrects)) / len(corrects)

        passed = 'Молодец, ответ принят, - правильно :)'
        notPassed = 'К сожалению, мне твой ответ показался неверным'
        print(mark)
        print(passed if mark > 0.75 else notPassed)