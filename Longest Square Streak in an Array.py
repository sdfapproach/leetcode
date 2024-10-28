# https://leetcode.com/problems/longest-square-streak-in-an-array/?envType=daily-question&envId=2024-10-28
# Longest Square Streak in an Array

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        num_to_index = {num: i for i, num in enumerate(nums)}
        dp = [1] * len(nums)

        max_len = 0

        for i in range(len(nums)):
            current = nums[i]
            streak_len = 1

            while current ** 2 in num_to_index:
                next_index = num_to_index[current ** 2]
                streak_len += 1
                dp[next_index] = max(dp[next_index], streak_len)
                current = nums[next_index]

            max_len = max(max_len, streak_len)

        return max_len if max_len >= 2 else -1