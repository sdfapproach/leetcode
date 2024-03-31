# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/?envType=daily-question&envId=2024-03-31
# Count Subarrays With Fixed Bounds

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        # count = 0
        
        # for i in range(len(nums)):
            
        #     min_flag = False
        #     max_flag = False

        #     for j in range(i, len(nums)):

        #         if nums[j] > maxK or nums[j] <minK:
        #             break

        #         if nums[j] == minK:
        #             min_flag = True
        #         if nums[j] == maxK:
        #             max_flag = True

        #         if max_flag and min_flag:
        #             count += 1

        # return count

        def countWindow(arr):
            min_pos = -1
            max_pos = -1
            count = 0
            for i, num in enumerate(arr):
                if num == minK:
                    min_pos = i
                if num == maxK:
                    max_pos = i
                if min_pos != -1 and max_pos != -1:
                    count += min(min_pos, max_pos) + 1
            return count
        
        total_count = 0
        start = 0
        for i in range(len(nums) + 1):
            if i == len(nums) or nums[i] < minK or nums[i] > maxK:
                if start < i:
                    total_count += countWindow(nums[start:i])
                start = i + 1
        
        return total_count