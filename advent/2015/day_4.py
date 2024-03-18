from day_4_data import strings

""" --- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice? """


def naughty_or_nice(s):
    vowels = {"a", "e", "i", "o", "u"}
    naughty_substrings = {"ab", "cd", "pq", "xy"}
    nice = 0
    s_list = s.splitlines()
    for s in s_list:
        double_letter, naughty = False, False
        if sum(s.count(v) for v in vowels) < 3:
            continue
        for i in range(len(s) - 1):
            if s[i : i + 2] in naughty_substrings:
                naughty = True
                break
        if naughty:
            continue
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                double_letter = True
                nice += 1
                break
    return nice


# print(
#     naughty_or_nice(
#         """ugknbfddgicrmopn
# aaa
# jchzalrnumimnmhp
# haegwjzuvuyypxyu
# dvszwmarrgswjxmb"""
#     )
# )  # * Expected == 2
print(naughty_or_nice(strings))  # * Expected == 238
