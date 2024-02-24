def sum_divisible_by_k(nums, target):
    output = 0
    i, j = 0, len(nums) - 1
    while i < j:
        while j > i:
            if (nums[j] + nums[i]) % target == 0:
                output += 1
            j -= 1
        j = len(nums) - 1
        i += 1
    return output


print(sum_divisible_by_k([1, 2, 3, 4, 5], 3))  # Expect 4
