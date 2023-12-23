# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2023-12-22
# Maximum Score After Splitting a String

class Solution:
    def maxScore(self, s: str) -> int:
        max = 0

        for i in range(len(s)-1):
            left = s[:i+1]
            right = s[i+1:]

            zero = 0
            one = 0

            for num in left:
                if num == '0':
                    zero += 1
            for num in right:
                if num == '1':
                    one += 1
            
            if zero + one > max:
                max = zero + one

        return max