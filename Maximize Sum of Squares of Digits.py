# https://leetcode.com/problems/maximize-sum-of-squares-of-digits/?envType=daily-question&envId=2026-10-14
# Maximize Sum of Squares of Digits

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        
        if sum > num * 9:
            return ""

        answer = []

        for _ in range(num):
            digit = min(9, sum)
            answer.append(str(digit))
            sum -= digit

        return "".join(answer)