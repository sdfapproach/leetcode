# https://leetcode.com/problems/binary-subarrays-with-sum/?envType=daily-question&envId=2024-03-14
# Binary Subarrays With Sum

from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # count = 0

        # for i in range(len(nums)):
        #     s = 0

        #     for j in range(goal, len(nums[i:])):

        #         if sum(nums[i:j+i+1]) == goal:
        #             count += 1
        #         elif sum(nums[i:j+i+1]) > goal:
        #             continue
        
        # return count

        count = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        curr_sum = 0

        for num in nums:
            curr_sum += num
            count += prefix_sum[curr_sum - goal]
            prefix_sum[curr_sum] += 1

        return count