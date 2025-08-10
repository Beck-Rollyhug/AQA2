# **Задача 1: Анаграмма**

# **Описание:**

# Напишите функцию **`is_anagram(s1, s2)`**, которая проверяет, являются ли две строки анаграммами (перестановками друг друга).

# **Требования:**

# - Функция должна принимать два аргумента: строки **`s1`** и **`s2`**.
# - Игнорируйте регистр символов.
# - Верните **`True`**, если строки являются анаграммами, иначе — **`False`**.

# **Пример:**

# print(is_anagram("listen", "silent"))  # True
# print(is_anagram("hello", "world"))    # False


def is_anagram(str1: str, str2: str):
    sort_str1 = ''.join(sorted(str1))
    sort_str2 = ''.join(sorted(str2))
    return sort_str1 == sort_str2

# ### **Задача 2: Палиндром**

# **Описание:**

# Напишите функцию **`is_palindrome(s)`**, которая проверяет, является ли строка палиндромом (читается одинаково слева направо и справа налево). Игнорируйте пробелы, знаки препинания и регистр.

# **Требования:**

# - Функция должна принимать один аргумент: строку **`s`**.
# - Верните **`True`**, если строка является палиндромом, иначе — **`False`**.

# **Пример:**

# is_palindrome("A man, a plan, a canal: Panama")  # True

# is_palindrome("racecar")                         # True

# is_palindrome("hello")                           # False


def is_palindrome(str: str):
    string = str.strip()
    is_even = len(string) % 2 == 0
    half_len = int(len(string) / 2)
    middle = half_len if is_even else half_len + 1
    first_half = sorted(string[0: half_len])
    second_half = sorted(string[middle: len(string)])
    return ''.join(first_half) == ''.join(second_half)


# **Задача 3: Самое длинное слово**

# **Описание:**

# Напишите функцию **`longest_word(s)`**, которая возвращает самое длинное слово в строке.

# **Требования:**

# - Функция должна принимать один аргумент: строку **`s`**.
# - Верните самое длинное слово.

# **Пример:**

# longest_word("In the middle of a vast desert, an extraordinary adventure awaits")  # "extraordinary”

def longest_word(string: str):
    words = string.split(' ')
    max_word = ''
    for word in words:
        if len(word) > len(max_word):
            max_word = word
    return max_word


# ### **Задача 4: Форматирование номера телефона**

# **Описание:**

# Напишите функцию **`format_phone_number(digits)`**, которая принимает строку из 10 цифр и возвращает её в формате **`(XXX) XXX-XXXX`**.

# **Требования:**

# - Функция должна принимать один аргумент: строку **`digits`**.
# - Верните отформатированный номер телефона.

# **Пример:**

# print(format_phone_number("1234567890"))  # "(123) 456-7890”

def format_phone_number(digits: str):
    return f"({digits[0:3]}) {digits[3:6]}-{digits[6:]}"

# **Задача 5: Удаление дублирующих символов**

# **Описание:**

# Напишите функцию **`remove_duplicates(s)`**, которая принимает строку и возвращает новую строку, из которой удалены все повторяющиеся символы, оставляя только первое вхождение каждого символа.

# **Требования:**

# - Функция должна принимать один аргумент: строку **`s`**.
# - Верните строку без повторяющихся символов.

# **Пример:**

# remove_duplicates("programming")  # "progamin”


def remove_duplicates(string: str):
    return ''.join(list(dict.fromkeys(string)))
    # set не сохраняет порядок элементов, поэтому использовал ключи словаря

# **Задача 6: Проверка на уникальность символов**

# Напишите функцию **`is_unique(s)`**, которая проверяет, содержит ли заданная строка все уникальные символы (без повторов).

# **Требования:**

# - Функция должна принимать один аргумент: строку **`s`**.
# - Верните **`True`**, если все символы уникальны, иначе — **`False`**.

# **Пример:**

# is_unique("abcdef")  # True
# is_unique("hello")  # False


def is_unique(string: str):
    return len(set(string)) == len(string)
