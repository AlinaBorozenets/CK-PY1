def get_unique_list_numbers() -> list[int]:
    import random
    a = -10
    b = 10
    range = [random.randint(a, b)]

    while len(range) < 15:
        i = random.randint(a, b)
        if i not in range:
            range.append(i)
    return range


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))