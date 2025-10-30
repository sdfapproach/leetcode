# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/?envType=daily-question&envId=2025-10-30
# Minimum Number of Increments on Subarrays to Form a Target Array

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
        ans = target[0]

        for a, b in zip(target, target[1:]):
            if a < b:
                ans += b - a

        return ans