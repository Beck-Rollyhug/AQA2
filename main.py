
# from Practice1.basic_info import task1
# from Practice1.user_profile import task2
# from Practice1.test_case_stats import task3
# from Practice1.bug_reports import task4
# from Practice1.bug_details import task5

# from Practice2.functions_intro import task6
# from Practice2.age_message import task7
# from Practice2.number_sum import task8
# from Practice2.triangle_check import task9
# from Practice2.nested_functions import task10

# from python_basic.AQA_course.homework_functions.number_sum import numbers_sum
# from python_basic.AQA_course.homework_functions.multiplication_table import multiplication_table
# from python_basic.AQA_course.homework_functions.bubble_sort import sort_task
# from python_basic.AQA_course.homework_functions.more_functions import count_items
# from python_basic.AQA_course.big_practice.strings import is_anagram, is_palindrome, format_phone_number, remove_duplicates, is_unique
# from python_basic.AQA_course.big_practice.lists import remove_duplicates, generate_squares, merge_lists, is_sorted, sum_lists_elements
from python_basic.AQA_course.big_practice.dicts import char_frequency, merge_dicts, dict_to_lists, group_by_first_letter, extract_subdict
from python_basic.AQA_course.big_practice.sets import get_unique_elements, is_unique_list, get_unique_vowels

from OOP.oop import CheckingAccount
from Booker.tests.test_booking import TestBooking
from Playwright.test_front import start_front_test
from Booker.constant import BASE_URL

# print(is_anagram('abc', 'cab'))
# print(is_palindrome('r ac car'))
# print(format_phone_number('1234567890'))
# print(remove_duplicates('programming'))
# print(is_unique('hello'))

# print(remove_duplicates([1, 2, 2, 3, 4, 4]))
# print(generate_squares(5))
# print(merge_lists([1, 2, 3], [3, 4, 5]))
# print(is_sorted([1, 3, 2, 4, 5]))
# print(sum_lists_elements([1, 2, 3], [4, 5, 6]))

# print(char_frequency('hello'))
# dict1 = {"a": 1, "b": 2}
# dict2 = {"b": 3, "c": 4}
# print(merge_dicts(dict1, dict2))  # {"a": 1, "b": 5, "c": 4}
# my_dict = {"a": 1, "b": 2, "c": 3}
# print(dict_to_lists(my_dict))  # (["a", "b", "c"], [1, 2, 3])
# strings = ["apple", "apricot", "banana", "blueberry", "cherry"]
# print(group_by_first_letter(strings))
# # {"a": ["apple", "apricot"], "b": ["banana", "blueberry"], "c": ["cherry"]}
# my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
# keys = ["a", "c"]
# print(extract_subdict(my_dict, keys))  # {"a": 1, "c": 3}

print(get_unique_elements([1, 2, 2, 3, 4, 4, 4, 5]))  # [1, 2, 3, 4, 5]
print(is_unique_list([1, 2, 3, 4]))  # True
print(is_unique_list([1, 2, 2, 3]))  # False
print(get_unique_vowels("Hello World"))  # {'e', 'o'}

# numbers_sum()
# multiplication_table()
# sort_task()
# count_items(1, 2, 3)

# Базовые задания на Python
# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
# task7()
# task8()
# task9()
# task10()
#

# Задание с ООП
# savingsAccount = CheckingAccount('Alex', 500)
# savingsAccount.withdraw(100)
# savingsAccount.test_balance()
# savingsAccount.apply_interest()
#

# Задание с restful-booker
# booker = TestBooking(BASE_URL)
# booker.test_all()
#

# Задание с Playwright
# start_front_test()
#
