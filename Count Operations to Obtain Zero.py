# https://leetcode.com/problems/count-operations-to-obtain-zero/?envType=daily-question&envId=2025-11-09
# Count Operations to Obtain Zero

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        
        if num1 == 0 or num2 == 0:
            return 0

        count = 0

        while num1-num2 != 0:
            count += 1
            
            if num1 > num2:
                num1 = num1-num2
            else:
                num2 = num2-num1
        
        return count+1