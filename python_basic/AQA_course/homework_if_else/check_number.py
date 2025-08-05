def check_number(number: int):
    positive = number >= 0
    even = number % 2 == 0

    if (positive and even):
        print(f"Число {number} положительное и чётное.")
    elif (not positive):
        print(f"Число {number} отрицательное.")
