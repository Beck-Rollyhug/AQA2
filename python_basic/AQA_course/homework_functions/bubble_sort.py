def get_nums_array_from(str: str, with_sep):
    return [int(substr) for substr in str.split(with_sep)]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def sort_task():
    nums_str = input('Введите числа через запятую: ')
    nums_array = get_nums_array_from(nums_str, with_sep=', ')
    print(f"Отсортированный список: {bubble_sort(nums_array)}")
