# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/?envType=daily-question&envId=2025-09-16
# Replace Non-Coprime Numbers in Array

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        
        stack = []
      
        for num in nums:
            stack.append(num)
          
            while len(stack) > 1:
                second_last, last = stack[-2:]
              
                common_divisor = gcd(second_last, last)
              
                if common_divisor == 1:
                    break
              
                stack.pop()
              
                stack[-1] = second_last * last // common_divisor
      
        return stack