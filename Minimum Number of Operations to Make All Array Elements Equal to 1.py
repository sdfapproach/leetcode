# https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/?envType=daily-question&envId=2025-11-12
# Minimum Number of Operations to Make All Array Elements Equal to 1

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        ones = nums.count(1)
        if ones > 0:
            return n - ones

        minOps = math.inf

        for i, g in enumerate(nums):
            for j in range(i + 1, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    minOps = min(minOps, j - i)
                    break

        return -1 if minOps == math.inf else minOps + n - 1