from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Solution 1, 25/312... not finding enough combinations
        cleaned_nums = sorted(nums)
        output = []
        i, j = 0, 3
        print(cleaned_nums)
        while j > len(cleaned_nums):
            total = sum(cleaned_nums[i:j])
            if total < 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                output.append([nums[i], nums[j], nums[k]])
            i += 1
            j = i + 1
            k = len(cleaned_nums) - 1
        return output

        # Solution 1, 25/312... not finding enough combinations. Slicing?
        cleaned_nums = sorted(nums)
        output = []
        i, j, k = 0, 1, len(cleaned_nums) - 1
        while j > k:
            total = nums[i] + nums[j] + nums[k]
            if total > 0:
                k -= 1
            elif total < 0:
                j += 1
            else:
                output.append([nums[i], nums[j], nums[k]])
            i += 1
            j = i + 1
            k = len(cleaned_nums) - 1
        return output


test = Solution()
print(test.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
