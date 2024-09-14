# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/?envType=daily-question&envId=2024-09-14
# Longest Subarray With Maximum Bitwise AND

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        k = max(nums)
        max_length = 0
        current_length = 0
        current_and = k

        for num in nums:
            if num & k != k:
                current_length = 0
                current_and = k
                continue

            current_and &= num
            if current_and == k:
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                current_length = 0
                current_and = k

        return max_length