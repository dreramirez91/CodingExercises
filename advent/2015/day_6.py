from day_6_data import directions


def christmas_lights(config):

    # ! Approach 1

    # * Initial Setup of lights ✅

    row = []
    lights = []
    i, j = 0, 0
    while i < 1000:
        row = []
        while j < 1000:
            row.append(False)
            j += 1
        lights.append(row)
        i += 1
        j = 0

    # ! In Python, when you append a list to another list,
    # ! you're appending a reference to that list, not a copy of it.
    # ! So, when you're appending the row list to lights, all rows in
    # ! lights end up referring to the same list object. To solve this
    # ! you need to create a new row variable for each iteration of the loop.

    # * Parsing the instructions

    directions = config.splitlines()
    for d in directions:
        direction = d.split(",")
        start_row, start_column = int(direction[0].split(" ")[-1]), int(
            direction[1].split(" ")[0]
        )
        end_row, end_column = int(direction[1].split(" ")[-1]), int(direction[2])
        # print(direction)
        # print(start_row, start_column, end_row, end_column, "\n")

        while start_row <= end_row:
            lights_to_change = lights[start_row][start_column : end_column + 1]
            if "turn on" in d:
                lights[start_row][start_column : end_column + 1] = [
                    True for _ in lights_to_change
                ]
            elif "turn off" in d:
                lights[start_row][start_column : end_column + 1] = [
                    False for _ in lights_to_change
                ]
            elif "toggle" in d:
                lights[start_row][start_column : end_column + 1] = [
                    not b for b in lights_to_change
                ]
            start_row += 1
    count = sum(sub_list.count(True) for sub_list in lights)
    return count

    # ! Approach 2

    # * Initial Setup of lights

    row = []
    lights = []
    i, j = 0, 0
    while i < 4:
        row = []
        while j < 4:
            row.append(False)
            j += 1
        lights.append(row)
        i += 1
        j = 0

    # * Parsing the instructions

    directions = config.splitlines()
    for d in directions:
        direction = d.split(",")
        print(direction)
        start_row, start_column = int(direction[0].split(" ")[-1]), int(
            direction[1].split(" ")[0]
        )
        end_row, end_column = int(direction[1].split(" ")[-1]), int(direction[2])

        print(start_row, start_column, end_row, end_column)
        print(lights[0])
        for row in range(start_row, end_row + 1):
            for col in range(start_column, min(end_column + 1, len(lights[0]))):
                print(col)
                if "turn on" in d:
                    lights[row][col] = True
                elif "turn off" in d:
                    lights[row][col] = False
                elif "toggle" in d:
                    lights[row][col] = not lights[row][col]
        count = sum(sub_list.count(True) for sub_list in lights)
    return count


print(christmas_lights(directions))
