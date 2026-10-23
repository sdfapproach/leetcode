# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/?envType=daily-question&envId=2026-10-23
# Maximum K to Sort a Permutation

class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        
        answer = -1

        for i, num in enumerate(nums):
            if i != num:
                if answer == -1:
                    answer = num
                else:
                    answer &= num

        return 0 if answer == -1 else answer