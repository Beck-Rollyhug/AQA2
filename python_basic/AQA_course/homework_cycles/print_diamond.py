def print_diamond(rows: int):
    cur = ['*']
    while len(cur) <= len(rows):
        print('\t'.join(cur))
        cur.append('*')

    while len(cur) > 0:
        cur.remove(0)
        print('\t'.join(cur))
