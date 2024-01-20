from day_1_data import calibration_document

# Day 1: Trebuchet

# Part One

# def calibrate(doc):
#     total = 0
#     for line in calibration_document.splitlines():
#         digit = ""
#         # Finds first digit in the line and adds its char to the digit string
#         for i in range(len(line)):
#             if line[i].isdigit():
#                 digit += line[i]
#                 break
#         # Finds last digit in the line and add its char to the digit string
#         for i in range(len(line) - 1, -1, -1):
#             if line[i].isdigit():
#                 digit += line[i]
#                 break
#         total += int(digit)
#     return total

# print(calibrate(calibration_document))

# Part Two

def calibrate_2(
    doc,
):
    word_nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    total = 0
    for line in doc.splitlines():
        digit = ""
        word_locations = []
        reversed_word_locations = []
        for word in word_nums:
            if word in line:
                word_locations.append(
                    (line.index(word), word)
                )  # This gets you only the first occurrence of the word
        for word in word_nums:
            reversed_word = word[::-1]
            if reversed_word in line[::-1]:
                reversed_word_locations.append([line[::-1].index(reversed_word), word])
        ordered_word_locations = sorted(word_locations, key=lambda a: a[0])
        ordered_reversed_word_locations = sorted(
            reversed_word_locations, key=lambda a: a[0]
        )
        for word in ordered_reversed_word_locations:
            word[0] = len(line) - word[0] - len(word[1])
        if ordered_word_locations:
            first_str_instance = ordered_word_locations[0][0]
        else:
            first_str_instance = float("inf")
        if ordered_reversed_word_locations:
            last_str_instance = ordered_reversed_word_locations[0][0]
            print(last_str_instance)
        else:
            last_str_instance = float("-inf")
        for i in range(len(line)):
            if line[i].isdigit():
                first_num_instance = i
                this_first_num_instance = line[i]
                break
            else:
                first_num_instance = 0
        if first_str_instance < first_num_instance:
            digit += word_nums[ordered_word_locations[0][1]]
        else:
            digit += this_first_num_instance
        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                second_num_instance = i
                print(second_num_instance)
                this_second_num_instance = line[i]
                break
        if last_str_instance > second_num_instance:
            digit += word_nums[ordered_reversed_word_locations[0][1]]
        else:
            digit += this_second_num_instance
        total += int(digit)
    return total


print(calibrate_2(calibration_document))
