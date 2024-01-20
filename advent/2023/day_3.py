from day_3_data import advent_data

import re


sample_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# Write down three ways of doing it before doing it
# Should have 12 finds for digits diagonal
# LOOK FOR SYMBOLS AND BASE IT ON THAT


# def engine_parts(schematic):
#     schematic = schematic.splitlines()
#     all_digit_locations = []
#     all_symbol_locations = []
#     for line in schematic:
#         digit = ""
#         digit_locations = []
#         symbol_locations = []
#         for i in range(len(line)):  # check and clean up these conditionals
#             if (i == len(line) - 1) and line[i].isdigit() and not digit:
#                 digit += line[i]
#                 digit_locations.append({(i - 1, i): int(digit)})
#                 digit = ""
#             elif line[i].isdigit():
#                 digit += line[i]
#             elif digit:
#                 # print(digit)  # problem is here somewhere...
#                 if line[i].isdigit() is False and line[i] != ".":
#                     symbol_locations.append(i)
#                 # print(re.search(digit, line))
#                 location = re.search(digit, line).span()
#                 # print(location)
#                 off_limits_range = []
#                 for i in range(location[0], location[1]):
#                     off_limits_range.append(i)
#                 if off_limits_range[0] != 0:
#                     off_limits_range.insert(0, off_limits_range[0] - 1)
#                 if off_limits_range[-1] != (len(line) - 1):
#                     off_limits_range.append(off_limits_range[-1] + 1)
#                 digit_locations.append({tuple(off_limits_range): int(digit)})
#                 digit = ""
#             if line[i].isdigit() is False and line[i] != ".":
#                 symbol_locations.append(i)
#         if digit_locations:
#             all_digit_locations.append((digit_locations))
#         else:
#             all_digit_locations.append([])
#         if symbol_locations:
#             all_symbol_locations.append((symbol_locations))
#         else:
#             all_symbol_locations.append([])
#     print("DIGITS:", all_digit_locations, "SYMBOLS:", all_symbol_locations)
#     parts = []
#     for symbol_line, i in zip(all_symbol_locations, range(len(all_digit_locations))):
#         for symbol_index in symbol_line:
#             for location_ranges in all_digit_locations[i]:
#                 for digit_location in location_ranges.keys():
#                     if symbol_index in digit_location:
#                         parts.append(location_ranges[digit_location])
#             for location_ranges_2 in all_digit_locations[i + 1]:
#                 for digit_location in location_ranges_2.keys():
#                     if symbol_index in digit_location:
#                         parts.append(location_ranges_2[digit_location])
#             for location_ranges_3 in all_digit_locations[i - 1]:
#                 for digit_location in location_ranges_3.keys():
#                     if symbol_index in digit_location:
#                         parts.append(location_ranges_3[digit_location])
#     return sum(parts)


# print(engine_parts(sample_data))  # Expected output = 4361

# 528577 incorrect, 529981


# def engine_parts(schematic):
#     schematic = schematic.splitlines()
#     all_symbol_locations = []
#     for line in schematic:
#         symbol_locations = []
#         for i in range(len(line)):  # check and clean up these conditionals
#             if line[i].isdigit() is False and line[i] != ".":
#                 symbol_locations.append(i)
#         if symbol_locations:
#             all_symbol_locations.append((symbol_locations))
#         else:
#             all_symbol_locations.append([])
#     print(all_symbol_locations)
#     parts = []
#     # try to avoid looping through the thing you are checking against :O ;(((((())))))
#     for i in range(len(schematic)):
#         line = schematic[i]  # for each line
#         digit = ""
#         for j in range(len(schematic[i])):  # for each char in line
#             if schematic[i][j].isdigit():
#                 digit += schematic[i][j]
#             elif digit:
#                 print(digit)
#                 try:
#                     location = re.search(digit, line).span()
#                     off_limits_range = []
#                     for i in range(location[0], location[1]):
#                         off_limits_range.append(i)
#                     if off_limits_range[0] != 0:
#                         off_limits_range.insert(0, off_limits_range[0] - 1)
#                     if off_limits_range[-1] != (len(line) - 1):
#                         off_limits_range.append(off_limits_range[-1] + 1)
#                     digit = ""
#                 except AttributeError:
#                     pass
# try:
#     if (
#         any(schematic[i].index(str(d for d in digit))
#         in all_symbol_locations[i - 1]
#         or j in all_symbol_locations[i + 1]
#     ):
#         print("got one", schematic[i][j], i, j)
#     if (
#         j + 1 in all_symbol_locations[i]
#         or j + 1 in all_symbol_locations[i - 1]
#         or j + 1 in all_symbol_locations[i + 1]
#     ):
#         print("got one", schematic[i][j], i, j)
#     if (
#         j - 1 in all_symbol_locations[i]
#         or j - 1 in all_symbol_locations[i - 1]
#         or j - 1 in all_symbol_locations[i + 1]
#     ):
#         print("got one", schematic[i][j], i, j)
# except IndexError:
#     pass
#     print("\n")
# return sum(parts)


# print(engine_parts(sample_data))


def engine_parts(schematic):
    schematic = schematic.splitlines()
    all_symbol_locations = []
    for line in schematic:
        symbol_locations = []
        for i in range(len(line)):  # check and clean up these conditionals
            if line[i].isdigit() is False and line[i] != ".":
                symbol_locations.append(i)
        if symbol_locations:
            all_symbol_locations.append((symbol_locations))
        else:
            all_symbol_locations.append([])
    all_symbol_locations.append([])  # Work around because I don't understand loops...
    print(all_symbol_locations)
    engine_parts = []
    for i in range(len(schematic)):  # for each line
        for j in range(len(schematic[i])):  # for each char in line
            if schematic[i][j].isdigit():  # if that character is a digit
                try:  # see if that digit is in the radius of a symbol
                    if (
                        j in all_symbol_locations[i - 1]
                        or j in all_symbol_locations[i + 1]
                    ):
                        start, end = j, j + 1
                        while schematic[i][j + 1].isdigit():
                            print(schematic[i][j + 1])  # slicing
                            end += 1
                            j += 1
                        while schematic[i][j - 1].isdigit():
                            print(schematic[i][j - 1])
                            start -= 1
                            j -= 1
                        digit = schematic[i][start:end]
                        print("DIGIT", digit)
                        engine_parts.append(digit)
                    elif (
                        j + 1 in all_symbol_locations[i]
                        or j + 1 in all_symbol_locations[i - 1]
                        or j + 1 in all_symbol_locations[i + 1]
                    ):
                        start, end = j, j + 1
                        while schematic[i][j + 1].isdigit():  # slicing
                            end += 1
                            j += 1
                        while schematic[i][j - 1].isdigit():
                            start -= 1
                            j -= 1
                        digit = schematic[i][start:end]
                        print("DIGIT", digit)
                        engine_parts.append(digit)
                    elif (
                        j - 1 in all_symbol_locations[i]
                        or j - 1 in all_symbol_locations[i - 1]
                        or j - 1 in all_symbol_locations[i + 1]
                    ):
                        start, end = j, j + 1
                        while schematic[i][j + 1].isdigit():  # slicing
                            end += 1
                            j += 1
                        while schematic[i][j - 1].isdigit():
                            start -= 1
                            j -= 1
                        digit = schematic[i][start:end]
                        print("DIGIT", digit)
                        engine_parts.append(digit)

                except IndexError:
                    pass
    print(engine_parts)
    # return sum(engine_parts)


print(engine_parts(sample_data))


# def engine_parts(schematic):
#     schematic = schematic.splitlines()
#     count = 0
#     all_symbol_locations = []
#     for line in schematic:
#         symbol_locations = []
#         for i in range(len(line)):  # check and clean up these conditionals
#             if line[i].isdigit() is False and line[i] != ".":
#                 symbol_locations.append(i)
#         if symbol_locations:
#             all_symbol_locations.append((symbol_locations))
#         else:
#             all_symbol_locations.append([])
#     all_symbol_locations.append([])
#     engine_parts = []
#     for i in range(len(schematic)):  # for each line
#         j = 0
#         while j < len(schematic[i]):  # for each char in line
#             if schematic[i][j].isdigit():
#                 digit = schematic[i][j]
#                 while schematic[i][j + 1].isdigit():
#                     digit += schematic[i][j + 1]
#                     j += 1
#                 print(digit)
#                 try:  # see if that digit is in the radius of a symbol
#                     if (
#                         j in all_symbol_locations[i - 1]
#                         or j in all_symbol_locations[i + 1]
#                     ):
#                         k = j
#                         digit = schematic[i][k]
#                         print(digit)
#                         while schematic[i][k + 1].isdigit():
#                             digit += schematic[i][k + 1]
#                             k += 1
#                         print(digit, i, j)
#                         # engine_parts.append(int(digit))
#                         # print(digit)
#                         digit = ""

#                     elif (
#                         j + 1 in all_symbol_locations[i]
#                         or j + 1 in all_symbol_locations[i - 1]
#                         or j + 1 in all_symbol_locations[i + 1]
#                     ):
#                         count += 1
#                         # engine_parts.append(int(digit))
#                         # print(digit)
#                         digit = ""

#                     elif (
#                         j - 1 in all_symbol_locations[i]
#                         or j - 1 in all_symbol_locations[i - 1]
#                         or j - 1 in all_symbol_locations[i + 1]
#                     ):
#                         count += 1
#                         # engine_parts.append(int(digit))
#                         # print(digit)
#                         digit = ""

#                 except IndexError:
#                     pass
#             j += 1
#     print(count)
#     return sum(engine_parts)


# print(engine_parts(sample_data))


# # try to avoid looping through the thing you are checking against :O ;(((((())))))
