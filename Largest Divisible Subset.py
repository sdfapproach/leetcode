# https://leetcode.com/problems/largest-divisible-subset/?envType=daily-question&envId=2024-02-09
# Largest Divisible Subset

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()
        dp = [1] * len(nums)
        parent = [-1] * len(nums)
        max_len = 0
        max_len_index = 0

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            if dp[i] > max_len:
                max_len = dp[i]
                max_len_index = i

        result = []
        while max_len_index != -1:
            result.append(nums[max_len_index])
            max_len_index = parent[max_len_index]

        return result[::-1]