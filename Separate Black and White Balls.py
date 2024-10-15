# https://leetcode.com/problems/separate-black-and-white-balls/?envType=daily-question&envId=2024-10-15
# Separate Black and White Balls

class Solution:
    def minimumSteps(self, s: str) -> int:

        count_of_zeros = 0
        steps = 0
        
        for ball in s[::-1]:
            if ball == '0':
                count_of_zeros += 1
            elif ball == '1':
                steps += count_of_zeros
        
        return steps