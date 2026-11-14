# https://leetcode.com/problems/minimum-positive-sum-subarray/?envType=daily-question&envId=2026-11-14
# Minimum Positive Sum Subarray

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        
        n = len(nums)
        answer = float('inf')

        for length in range(l, r + 1):
            window_sum = sum(nums[:length])

            if window_sum > 0:
                answer = min(answer, window_sum)

            for i in range(length, n):
                window_sum += nums[i] - nums[i - length]

                if window_sum > 0:
                    answer = min(answer, window_sum)

        return -1 if answer == float('inf') else answer