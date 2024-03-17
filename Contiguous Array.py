# https://leetcode.com/problems/contiguous-array/?envType=daily-question&envId=2024-03-16
# Contiguous Array

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        # count = 0

        # for i in range(1, len(nums)):

        #     if nums[i] != nums[i-1]:
        #         count += 1
        
        # return count

        max_length = 0
        count = 0
        hashmap = {0: -1}
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            
            if count in hashmap:
                max_length = max(max_length, i - hashmap[count])
            else:
                hashmap[count] = i
        
        return max_length