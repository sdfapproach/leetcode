# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/description/?envType=daily-question&envId=2024-01-04
# Minimum Number of Operations to Make Array Empty

from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count_nums = Counter(nums)

        count = 0

        for n in count_nums.values():
            if n == 1:
                return -1

            if n%3 == 0:
                count += n//3
                continue
            else:
                count += n//3 + 1
            
        return count