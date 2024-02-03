from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        compare = ""
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                compare += t[i]
                j += 1
            i += 1
        return compare == s
