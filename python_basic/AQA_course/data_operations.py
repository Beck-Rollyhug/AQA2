# 1. Полное кол-во килограмм в заданном числе грамм
grams = 12345
kilo = int(grams // 1000)
print(f"В {grams} находится {kilo} полных килограмм")

# 2. Последняя цифра числа
num = 12345
last = num % 10
print(f"Последняя цифра в {num} равна {last}")

# 3. Положительное и четное
number = 14
isPos = number >= 0
isChet = number % 2 == 0
if isPos and isChet:
    print(f"Число {number} является положительным и четным")
elif isPos:
    print(f"Число {number} является положительным ")
elif isChet:
    print(f"Число {number} является четным")
else:
    print(f"Число {number} не является ни положительнымб ни четным")

# 4.Число в диапазоне
n = 50
if 0 < n and n < 100:
    print(f"Число {n} в пределах диапазона 0-100")
else:
    print(f"Число {n} не в пределах диапазона 0-100")

# 5.Не кратно 3
num5 = 9
if num5 % 3 == 0:
    print(f"Число {n} кратно 3")
else:
    print(f"Число {n} не кратно 3")
