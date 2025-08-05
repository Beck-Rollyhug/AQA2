def count_vowels(string: str):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in string:
        if char in vowels:
            count += 1

    print(f"Количество гласных в строке {string}: {count}")
