# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/?envType=daily-question&envId=2024-11-19
# Maximum Sum of Distinct Subarrays With Length K

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        # max_sum = 0

        # for i in range(len(nums)):

        #     sub_arr = nums[i:i+k]

        #     if len(set(sub_arr)) == k:
        #         max_sum = max(sum(sub_arr), max_sum)
            
        # return max_sum

        max_sum = 0
        current_sum = 0
        seen = set()
        start = 0
        
        for end in range(len(nums)):
            if nums[end] in seen:
                while nums[end] in seen:
                    seen.remove(nums[start])
                    current_sum -= nums[start]
                    start += 1
            
            seen.add(nums[end])
            current_sum += nums[end]
            
            if end - start + 1 == k:
                max_sum = max(max_sum, current_sum)
                seen.remove(nums[start])
                current_sum -= nums[start]
                start += 1
        
        return max_sum