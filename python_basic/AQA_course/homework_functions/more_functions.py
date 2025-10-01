def rectangle_area(a: int, b: int):
    return a*b


def convert_seconds(secs: int):
    return tuple(secs // 60 // 60, secs // 60)


def power_of(num: int, exp: int):
    return num**exp


def count_items(*args):
    return len(args)
