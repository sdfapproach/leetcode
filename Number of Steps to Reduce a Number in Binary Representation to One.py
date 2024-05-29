# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/?envType=daily-question&envId=2024-05-29
# Number of Steps to Reduce a Number in Binary Representation to One

class Solution:
    def numSteps(self, s: str) -> int:
        
        count = 0
        number = int(s, 2)

        while number > 1:
            if number % 2 ==0:
                number //= 2
            else:
                number += 1
            # number = number // 2 if number % 2 == 0 else number + 1
            count += 1

        return count