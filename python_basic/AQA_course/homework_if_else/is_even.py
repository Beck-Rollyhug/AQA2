def is_even(number: int):
    even = 'чётным' if number & 2 == 0 else 'нечётным'
    print(f"Число {number} является {even}.")
