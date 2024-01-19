from typing import List
import collections

# Solution 1
""" def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort() # Sorting time complexity is O(n log n) so that is the bottleneck for containsDuplicate
    for i in range(len(nums) - 1):
    if nums[i] == nums[i+1]:
        return True
    return False """

# Solution 2
""" def containsDuplicate(nums: List[int]) -> bool:
    no_duplicates = sorted(list(set(nums)))
    return no_duplicates != sorted(nums) """


# Solution 3
""" def containsDuplicate(nums: List[int]) -> bool:
    counts = dict(collections.Counter(nums))
    for count in counts.values():
        if count > 1:
            return True
    return False
 """

# Solution 4
""" def containsDuplicate(nums: List[int]) -> bool:
    for num in nums:
        if nums.count(num) > 1:
            return True
    return False """


""" # Solution 5 (most efficient)
def containsDuplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
 """

""" # Solution 5 (most efficient)
def containsDuplicate(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))
 """


# Solution 5
def containsDuplicate(nums):
    hashmap = {}
    for num in nums:
        if num not in hashmap:
            hashmap[num] = 0
        hashmap[num] += 1
        if hashmap[num] > 1:
            return True
    return False


print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

nums = (55, 44, 33, 22)
