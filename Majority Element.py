# https://leetcode.com/problems/majority-element/?envType=daily-question&envId=2024-02-12
# Majority Element

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)

        for key, value in count.items():
            if value > len(nums) / 2:
                return key