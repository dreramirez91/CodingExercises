from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start, end = 0, len(height) - 1
        while start < end:
            w = end - start
            h = min(height[start], height[end])
            if w * h > max_area:
                max_area = w * h
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_area
