# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/?envType=daily-question&envId=2026-07-16
# Sum of GCD of Formed Pairs

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        
        prefix_gcd = []
        current_max = 0

        for x in nums:
            current_max = max(current_max, x)
            prefix_gcd.append(gcd(x, current_max))

        prefix_gcd.sort()

        ans = 0
        left = 0
        right = len(prefix_gcd) - 1

        while left < right:
            ans += gcd(prefix_gcd[left], prefix_gcd[right])
            left += 1
            right -= 1

        return ans