import timeit

# # Enumerate worst-case time complexity is O(n)
# enumerate_time = timeit.timeit(
#     "for i, val in enumerate(lst): x += val", "x, lst = 0, [1,2,3,4]"
# )
# print(f"Enumerate time: {enumerate_time} seconds")

# # Range(len(iterable)) worst-case time complexity is O(n)
# range_time = timeit.timeit(
#     "for i in range(len(lst)): x += lst[i]", "x, lst= 0, [1,2,3,4]"
# )
# print(f"Range time: {range_time} seconds")

# RESULTS:
# Enumerate time: 0.20291979098692536 seconds
# Range time: 0.2211362500092946 seconds


def sum_of_squares_silva(values):
    if not values:
        return None
    count = 0
    for value in values:
        count += value**2
    return count


silvas_time = timeit.timeit(lambda: sum_of_squares_silva([1, 2, 3, 4, 5]))
print("Silva's time:", silvas_time)


def sum_of_squares_erika(values):
    if not values:
        return None
    squares = []
    for value in values:
        squares.append(value**2)
    return sum(squares)


erikas_time = timeit.timeit(lambda: sum_of_squares_erika([1, 2, 3, 4, 5]))
print("Erika's time:", erikas_time)
