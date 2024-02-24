def count_depth_increases(depths):
    previous_reading = sum(depths[0:3])
    ans = 0
    for i in range(len(depths) - 2):
        current_reading = sum(depths[i : i + 3])
        if sum(depths[i : i + 3]) > previous_reading:
            ans += 1
        previous_reading = current_reading
    return ans


print(count_depth_increases([199, 200, 208, 210, 200, 207, 240, 269, 260, 263]))
