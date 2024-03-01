# https://leetcode.com/problems/maximum-odd-binary-number/?envType=daily-question&envId=2024-03-01
# Maximum Odd Binary Number

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # count = 0

        # for char in s:
        #     if char == '1':
        #         count += 1

        # one = ['1'] * (count-1)
        # zero = ['0'] * (len(s) - count)
        
        # one += zero
        # one += ['1']

        # return "".join(one)

        ones_count = s.count('1')
        
        zeros_count = len(s) - ones_count

        result = '1' * (ones_count - 1) + '0' * zeros_count + '1'

        return result