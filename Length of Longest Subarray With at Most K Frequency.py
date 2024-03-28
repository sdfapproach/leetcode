# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/?envType=daily-question&envId=2024-03-28
# Length of Longest Subarray With at Most K Frequency

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        start = 0
        maxLength = 0
        frequency = {}

        for end in range(len(nums)):
            if nums[end] in frequency:
                frequency[nums[end]] += 1
            else:
                frequency[nums[end]] = 1

            while frequency[nums[end]] > k:
                frequency[nums[start]] -= 1
                start += 1
                
            maxLength = max(maxLength, end - start + 1)

        return maxLength