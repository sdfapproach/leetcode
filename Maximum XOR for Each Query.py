# https://leetcode.com/problems/maximum-xor-for-each-query/?envType=daily-question&envId=2024-11-08
# Maximum XOR for Each Query

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        xor_total = 0
        
        for num in nums:
            xor_total ^= num
        
        max_val = (1 << maximumBit) - 1
        
        answer = []
        
        for i in range(len(nums) - 1, -1, -1):
            answer.append(xor_total ^ max_val)
            xor_total ^= nums[i]

        return answer