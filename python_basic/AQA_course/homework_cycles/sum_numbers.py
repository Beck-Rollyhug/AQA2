def sum_numbers(n: int):
    count = 0
    sum = 0
    while count < n:
        count += 1
        sum += count

    print(f"Сумма чисел от 1 до {n}: {sum}")
