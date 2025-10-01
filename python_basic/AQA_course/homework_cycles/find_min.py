def find_min(numbers: list[int]):
    min = numbers[0]
    for num in numbers:
        if num < min:
            min = num

    print(f"Минимальное число в списке:  {min}")
