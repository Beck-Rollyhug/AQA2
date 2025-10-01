def check_grade(score: int):
    grade = 'Неудовлетворительно'

    if 90 < score and score <= 100:
        grade = 'Отлично'
    elif 75 < score and score <= 89:
        grade = 'Хорошо'
    elif 50 < score and score <= 74:
        grade = 'Удовлетворительно'

    print(f"Оценка за {score} баллов: {grade}.")
