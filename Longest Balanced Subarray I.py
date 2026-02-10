# https://leetcode.com/problems/longest-balanced-subarray-i/?envType=daily-question&envId=2026-02-10
# Longest Balanced Subarray I

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        
        n = len(nums)
        ans = 0

        for l in range(n):
            even = set()
            odd = set()
            for r in range(l, n):
                if nums[r] % 2 == 0:
                    even.add(nums[r])
                else:
                    odd.add(nums[r])

                if len(even) == len(odd):
                    ans = max(ans, r - l + 1)

        return ans