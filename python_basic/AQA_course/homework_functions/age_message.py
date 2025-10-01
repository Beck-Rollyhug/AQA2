def calculate(year):
    age = 2025 - year
    if age < 18:
        print(f"Вы еще молоды, учеба — ваш путь!")
    elif 18 <= age and age < 65:
        print(f"Отличный возраст для карьерного роста!")
    else:
        print(f"Пора наслаждаться заслуженным отдыхом!")


year = int(input('Введите год вашего рождения:'))
calculate(year)
