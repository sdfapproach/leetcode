# https://leetcode.com/problems/fraction-addition-and-subtraction/?envType=daily-question&envId=2024-08-23
# Fraction Addition and Subtraction

from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:

        fractions = []
        num = ""
        
        for i, char in enumerate(expression):
            if char in "+-" and i > 0:
                fractions.append(Fraction(num))
                num = char
            else:
                num += char

        fractions.append(Fraction(num))
        
        result = sum(fractions)
        
        return f"{result.numerator}/{result.denominator}"