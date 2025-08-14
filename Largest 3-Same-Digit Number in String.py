# https://leetcode.com/problems/largest-3-same-digit-number-in-string/?envType=daily-question&envId=2025-08-14
# Largest 3-Same-Digit Number in String

class Solution:
    def largestGoodInteger(self, num: str) -> str:

        digits = []

        count = 1
        number = ""

        for n in num:
            if number == n:
                count += 1
                if count >= 3:
                    digits.append(int(n))
                    count = 0
                    number = ""
            else:
                count = 1
                number = n
        
        if len(digits) == 0:
            return ""
        else:
            return str(max(digits)) * 3