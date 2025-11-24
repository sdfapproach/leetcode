# https://leetcode.com/problems/binary-prefix-divisible-by-5/?envType=daily-question&envId=2025-11-24
# Binary Prefix Divisible By 5

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        
        answer = []
        remainder = 0
        
        for bit in nums:
            remainder = (remainder * 2 + bit) % 5
            
            answer.append(remainder == 0)
            
        return answer