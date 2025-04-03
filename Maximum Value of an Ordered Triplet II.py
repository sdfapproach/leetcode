# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/?envType=daily-question&envId=2025-04-03
# Maximum Value of an Ordered Triplet II

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 3:
            return 0

        left_max = [float('-inf')] * n
        left_min = [float('inf')] * n
        for j in range(1, n):
            left_max[j] = max(left_max[j-1], nums[j-1])
            left_min[j] = min(left_min[j-1], nums[j-1])

        right_max = [float('-inf')] * n
        right_min = [float('inf')] * n
        for j in range(n-2, -1, -1):
            right_max[j] = max(right_max[j+1], nums[j+1])
            right_min[j] = min(right_min[j+1], nums[j+1])
        
        ans = float('-inf')
        for j in range(1, n-1):
            candidate1 = (left_max[j] - nums[j]) * right_max[j]
            candidate2 = (left_min[j] - nums[j]) * right_min[j]
            ans = max(ans, candidate1, candidate2)
        
        return ans if ans >= 0 else 0