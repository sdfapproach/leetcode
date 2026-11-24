# https://leetcode.com/problems/maximum-subarray-with-equal-products/?envType=daily-question&envId=2026-11-24
# Maximum Subarray With Equal Products

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        answer = 0

        for i in range(n):
            p = 1
            g = 0
            l = 1

            for j in range(i, n):
                p *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])

                if p == g * l:
                    answer = max(answer, j - i + 1)

        return answer