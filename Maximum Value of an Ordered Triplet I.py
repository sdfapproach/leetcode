# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/?envType=daily-question&envId=2025-04-02
# Maximum Value of an Ordered Triplet I

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n < 3:
            return 0

        best_max = [0] * n
        best_min = [0] * n
        best_max[0] = nums[0]
        best_min[0] = nums[0]
        for j in range(1, n):
            best_max[j] = max(best_max[j-1], nums[j-1])
            best_min[j] = min(best_min[j-1], nums[j-1])
        
        max_after = [0] * n
        min_after = [0] * n
        max_after[n-1] = nums[n-1]
        min_after[n-1] = nums[n-1]
        for j in range(n-2, -1, -1):
            max_after[j] = max(max_after[j+1], nums[j+1])
            min_after[j] = min(min_after[j+1], nums[j+1])
        
        ans = 0
        for j in range(1, n-1):
            diff1 = best_max[j] - nums[j]
            diff2 = best_min[j] - nums[j]
            if diff1 > 0 and max_after[j] > 0:
                ans = max(ans, diff1 * max_after[j])
            if diff2 < 0 and min_after[j] < 0:
                ans = max(ans, diff2 * min_after[j])
        
        return ans