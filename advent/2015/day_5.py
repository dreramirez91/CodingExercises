from day_4_data import strings


def naughty_or_nice(s):
    # * PART II
    """Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

    Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
    """
    nice = 0
    s_list = s.splitlines()
    for s in s_list:
        repeat, double = False, False
        for i in range(len(s) - 2):
            if s[i : i + 2] in s[i + 2 :]:
                repeat = True
            if s[i] == s[i + 2]:
                double = True
        if repeat and double:
            nice += 1
    return nice

    # * PART I
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

    vowels = {"a", "e", "i", "o", "u"}
    naughty_substrings = {"ab", "cd", "pq", "xy"}
    nice = 0
    s_list = s.splitlines()
    for s in s_list:
        naughty = False
        if len([c for c in s if c in vowels]) < 3:
            continue
        for i in range(len(s) - 1):
            if s[i : i + 2] in naughty_substrings:
                naughty = True
                break
        if naughty:
            continue
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
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
# )
print(naughty_or_nice(strings))

# print(
#     naughty_or_nice(
#         """qjhvhtzxzqqjkmpb
# xxyxx
# uurcxstgmygtbstg
# ieodomkazucvgmuy"""
#     )
# )
