# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/?envType=daily-question&envId=2026-07-07
# Concatenate Non-Zero Digits and Multiply by Sum I

class Solution:
    def sumAndMultiply(self, n: int) -> int:

        if n == 0:
            return 0
        
        non_zero_digits = ""
        some_digits = 0

        for c in str(n):
            if c != "0":
                non_zero_digits += c
                some_digits += int(c)

        return int(non_zero_digits) * some_digits

