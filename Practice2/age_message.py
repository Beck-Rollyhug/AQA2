def task7():
    year = int(input('Year of birth: '))
    age = 2025 - year
    print("Ваш возраст:", age)
    
    if age < 18:
        print("Вы еще молоды, учеба — ваш путь!")
    elif age <= 65:
        print("Отличный возраст для карьерного роста!")
    else:
        print("Пора наслаждаться заслуженным отдыхом!")

