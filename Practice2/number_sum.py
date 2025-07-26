def task8():
    num = int(input('n: '))
    i = 0
    string = ''
    sum = 0
    while i <= num:
        string += f'{i} '
        sum += i
        i += 1

    print('nums: ', string)
    print('sum: ', sum)