# https://leetcode.com/problems/count-complete-subarrays-in-an-array/?envType=daily-question&envId=2025-04-24
# Count Complete Subarrays in an Array

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        total_distinct = len(set(nums))
    
        left = 0
        distinct_count = 0
        count = 0
        freq = Counter()

        for right in range(len(nums)):
            freq[nums[right]] += 1
            
            while len(freq) == total_distinct:
                count += len(nums) - right
                
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

        return count