# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/?envType=daily-question&envId=2026-09-24
# Smallest Index With Digit Sum Equal to Index

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        def digit_sum(num):
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total

        for i, num in enumerate(nums):
            if i == digit_sum(num):
                return i

        return -1