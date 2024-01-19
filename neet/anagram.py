from collections import Counter

# Solution 1
""" 
def isAnagram(s: str, t: str) -> bool:
    return dict(Counter(s)) == dict(Counter(t))


print(isAnagram("anagram", "nagaram")) """

#  Solution 1a
""" 
def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


print(isAnagram("anagram", "nagaram")) """

# Solution 2
"""
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_count, t_count = {}, {}
    for i in range(len(s)):
        s_count[s[i]] = s_count.get(s[i], 0) + 1
        t_count[t[i]] = t_count.get(t[i], 0) + 1
    return s_count == t_count


print(isAnagram("rat", "car"))
 """

# Solution 3
""" 
def isAnagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


print(isAnagram("rat", "car"))
 """
