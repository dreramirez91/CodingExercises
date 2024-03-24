from typing import List


# ! No duplicates in the answer
# ! The answer is a nested list of numbers, not indices


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
        nums.sort()  # * Correct!
        print(nums)
        hashmap = {}
        i, j = 0, len(nums) - 1
        while i < j:
            hashmap[i, j] = nums[i] + nums[j]
            i += 1
            j -= 1
        print(hashmap)
        k = 0
        for k, indices, total in zip(
            range(len(nums)), hashmap.keys(), hashmap.values()
        ):
            if nums[k] + total == 0:
                ans = [k] + indices
                print(ans)
            # if k + sum()

        output = []
        return output


""" class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]
        cleaned_nums = sorted(nums)
        output = []
        i, j = 0, len(cleaned_nums) - 1
        hashmap = dict()
        print(cleaned_nums, "\n\n")
        while i < j:
            complement = 0 - cleaned_nums[i] - cleaned_nums[j]
            print("cleaned_nums[i]", "cleaned_nums[j]", "complement")
            print(
                "     ",
                cleaned_nums[i],
                "           ",
                cleaned_nums[j],
                "           ",
                complement,
            )
            print("\nhashmap:", hashmap)
            print("output:", output, "\n\n")
            if cleaned_nums[i] in hashmap:
                old_i, old_j = hashmap.get(cleaned_nums[i])
                if i != old_i:
                    output.append(
                        [cleaned_nums[i], cleaned_nums[old_i], cleaned_nums[old_j]]
                    )
            elif cleaned_nums[j] in hashmap:
                old_i, old_j = hashmap.get(cleaned_nums[j])
                if j != old_j:
                    output.append(
                        [cleaned_nums[i], cleaned_nums[old_i], cleaned_nums[old_j]]
                    )
            else:
                hashmap[complement] = (i, j)
            if cleaned_nums[i] < complement:
                i += 1
            else:
                j -= 1
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
 """

test = Solution()
print(test.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
