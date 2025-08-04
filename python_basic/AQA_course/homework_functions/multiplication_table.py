def get_row(num_multi=1):
    base_row = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    new_row = []
    for num in base_row:
        new_row.append(num * num_multi)

    return new_row


def print_row(row):
    row_str = '\t'.join([str(num) for num in row])
    print(row_str)


def multiplication_table():
    multi = 1
    limit = 10
    row = get_row()
    while multi <= limit:
        print_row(row)
        multi += 1
        row = get_row(multi)
