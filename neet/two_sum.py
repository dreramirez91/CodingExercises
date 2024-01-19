def two_sum(nums, target):
    # Solution 1
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return i, j"""

    # Solution 2
    """ hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = i
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and i != hashmap[complement]:
            return i, hashmap[complement] """

    # Solution 3
    """ for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums and nums.index(complement) != i:
            return i, nums.index(complement) """

    # Solution 4... Crucially, you don't to construct the entire data structure before looping, you can do it WHILE looping => Most efficient
    hashmap = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if (
            complement in hashmap
        ):  # Dictionary look up is constant time operation O(1).. to cut off an extra loop think (CAN I USE "IN" KEYWORD WITH DICTIONARY)
            return hashmap[complement], i
        hashmap[nums[i]] = i


print(two_sum([3, 2, 4], 6))
