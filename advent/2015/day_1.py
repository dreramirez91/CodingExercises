# ( means up
# ) means down
# starts at 0
from day_1_data import instructions


def which_floor(instructions):
    # Part 2
    floor = 0
    for i in range(len(instructions)):
        if instructions[i] == "(":
            floor += 1
        elif instructions[i] == ")":
            floor -= 1
        if floor == -1:
            return i + 1
    # Part 1
    floor = 0
    for instruction in instructions:
        if instruction == "(":
            floor += 1
        elif instruction == ")":
            floor -= 1
    return floor


print(which_floor(instructions))
