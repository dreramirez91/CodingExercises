from day_2_data import present_dimensions


# Part 1
def how_many_ft_wrapping_paper(present_dimensions):
    present_list = present_dimensions.splitlines()
    amount = 0
    for present in present_list:
        l, w, h = (int(d) for d in present.split("x"))
        amount += 2 * l * w + 2 * w * h + 2 * h * l
        smallest_side = min([(l * w), (w * h), (h * l)])
        amount += smallest_side
    return amount


# print(how_many_ft_wrapping_paper(present_dimensions))


# Part 2
def how_many_ft_ribbon(present_dimensions):
    present_list = present_dimensions.splitlines()
    amount = 0
    for present in present_list:
        l, w, h = (int(d) for d in present.split("x"))
        sides = [l, w, h]
        sides.remove(max(sides))
        amount += sum(sides) * 2
        bow = l * w * h
        amount += bow
    return amount


print(how_many_ft_ribbon(present_dimensions))
