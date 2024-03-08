# https://leetcode.com/problems/count-elements-with-maximum-frequency/?envType=daily-question&envId=2024-03-08
# Count Elements With Maximum Frequency

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        count = collections.Counter(nums)

        max_freq = 0
        max_val = 0

        for value in count.values():
            
            if value == max_val:
                max_freq += 1

            elif value > max_val:
                max_val = value
                max_freq = 1
        
        return max_freq * max_val