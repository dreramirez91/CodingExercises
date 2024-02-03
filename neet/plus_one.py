from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 10 and i != 0:
                digits[i] = 0
                digits[i - 1] += 1
            elif digits[i] == 10 and i == 0:
                digits[i] = 1
                digits.append(0)
            i -= 1
        return digits
