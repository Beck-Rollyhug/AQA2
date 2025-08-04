def calculate_with(num):
    sum = 1
    count = 1
    nums = [str(count)]
    while count < num:
        count += 1
        sum += count
        nums.append(str(count))
    return nums, sum


def print_all(nums, sum):
    nums_str = ' '.join(nums)
    print(f"Числа: {nums_str}")
    print(f"Сумма чисел: {sum}")


def numbers_sum():
    num = int(input('Введите число:'))
    nums, sum = calculate_with(num)
    print_all(nums, sum)
