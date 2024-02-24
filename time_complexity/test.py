from timeit import timeit

# Enumerate worst-case time complexity is O(n)
enumerate_time = timeit(
    "for i, val in enumerate(lst): x += val", "x, lst = 0, [1,2,3,4]"
)
print(f"Enumerate time: {enumerate_time} seconds")

# Range(len(iterable)) worst-case time complexity is O(n)
range_time = timeit("for i in range(len(lst)): x += lst[i]", "x, lst= 0, [1,2,3,4]")
print(f"Range time: {range_time} seconds")

# RESULTS:
# Enumerate time: 0.20291979098692536 seconds
# Range time: 0.2211362500092946 seconds
