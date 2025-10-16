# https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/?envType=daily-question&envId=2025-10-16
# Smallest Missing Non-negative Integer After Operations

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        
        cnt = [0] * value
        for a in nums:
            r = ((a % value) + value) % value  # safe mod for negatives
            cnt[r] += 1

        x = 0
        while cnt[x % value] > 0:
            cnt[x % value] -= 1
            x += 1
        return x