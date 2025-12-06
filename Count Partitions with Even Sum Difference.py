# https://leetcode.com/problems/count-partitions-with-even-sum-difference/?envType=daily-question&envId=2025-12-05
# Count Partitions with Even Sum Difference

class Solution:
    def countPartitions(self, nums: List[int]) -> int:

        count = 0
        
        for i in range(1, len(nums)):

            if (sum(nums[:i]) - sum(nums[i:])) % 2 == 0:
                count += 1

        return count
