# https://leetcode.com/problems/predict-the-winner/?envType=daily-question&envId=2026-08-01
# Predict the Winner

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        n = len(nums)
        dp = nums[:]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                take_left = nums[i] - dp[i + 1]
                take_right = nums[j] - dp[i]

                dp[i] = max(take_left, take_right)

        return dp[0] >= 0