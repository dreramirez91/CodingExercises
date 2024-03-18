from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Solution 3, optimal
        """notes: to use two pointers and loop once,
        while still accomplishing the goal,
        aim for more granular condition handling.
        That is, pointers are moved carefully based
        on problem logic implemented
        through the specificity of the conditionals."""
        i,     j = 0, len       (numbers) - 1
        while j > i:
            current_sum = (
                numbers[i] + numbers[j]
            )  # compute this only once rather than in each if-elif to improve runtime
            if current_sum > target:
                
                
                
                j -= 1
            elif current_sum == target:
                return i + 1, j + 1
            else:
                i += 1
        return
        # Solution 2, even worse
        i = 0
        j = 1
        while j < len(numbers):
            print(numbers[i], numbers[j])
            if numbers[i] + numbers[j] == target:
                return i + 1, j + 1
            if j + 1 == len(numbers) or numbers[j + 1] >= target:
                while True:
                    while i < j:
                        if numbers[i] + numbers[j] == target:
                            return i + 1, j + 1
                        i += 1
                    i = 0
                    j -= 1
            j += 1
        return
        # Solution 1, brute force. Don't iterate more than you have to.
        i, j = 0, 1
        while i < len(numbers):
            while j < len(numbers):
                if numbers[i] + numbers[j] > target:
                    break
                elif numbers[i] + numbers[j] == target:
                    return i + 1, j + 1
                j += 1
            i += 1
            j = i + 1


test = Solution()
print(test.twoSum([1, 3, 4, 5, 7, 10, 11], 9))
