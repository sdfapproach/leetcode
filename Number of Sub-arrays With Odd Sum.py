# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/?envType=daily-question&envId=2025-02-25
# Number of Sub-arrays With Odd Sum

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        mod = 10**9 + 7
        
        even = 1
        odd = 0
        prefix = 0
        ans = 0
        
        for num in arr:
            prefix = (prefix + num) % 2
            
            if prefix == 0:
                ans = (ans + odd) % mod
                even += 1
            else:
                ans = (ans + even) % mod
                odd += 1
        
        return ans