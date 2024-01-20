from day_3_data import advent_directions


def at_least_one_present(directions):
    # Solution 2
    at_least_one = 1
    been_there = [(0, 0)]
    santa_x, santa_y = 0, 0
    robot_x, robot_y = 0, 0
    for santa_direction in range(0, len(directions), 2):
        if directions[santa_direction] == "<":
            santa_x -= 1
        elif directions[santa_direction] == ">":
            santa_x += 1
        elif directions[santa_direction] == "v":
            santa_y -= 1
        elif directions[santa_direction] == "^":
            santa_y += 1
        santa_coordinates = santa_x, santa_y
        if santa_coordinates not in been_there:
            been_there.append(santa_coordinates)
            at_least_one += 1
    for robot_direction in range(1, len(directions), 2):
        if directions[robot_direction] == "<":
            robot_x -= 1
        elif directions[robot_direction] == ">":
            robot_x += 1
        elif directions[robot_direction] == "v":
            robot_y -= 1
        elif directions[robot_direction] == "^":
            robot_y += 1
        robot_coordinates = robot_x, robot_y
        if robot_coordinates not in been_there:
            been_there.append(robot_coordinates)
            at_least_one += 1
    return at_least_one
    # Solution 1
    at_least_one = 1
    x, y = 0, 0
    been_there = [(0, 0)]
    for direction in directions:
        if direction == "<":
            x -= 1
        elif direction == ">":
            x += 1
        elif direction == "v":
            y -= 1
        elif direction == "^":
            y += 1
        coordinates = x, y
        if coordinates not in been_there:
            been_there.append(coordinates)
            at_least_one += 1
    return at_least_one


print(at_least_one_present(advent_directions))
