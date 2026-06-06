# https://leetcode.com/problems/left-and-right-sum-differences/?envType=daily-question&envId=2026-06-06
# Left and Right Sum Differences

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        left = [0]

        for i in range(n-1):
            left.append(left[i] + nums[i])


        right = [0]

        for i in range(n-1):
            right.append(right[i] + nums[n-1-i])

        return [abs(left[i] - right[n-1-i]) for i in range(n)]