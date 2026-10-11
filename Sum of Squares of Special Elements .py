# https://leetcode.com/problems/sum-of-squares-of-special-elements/?envType=daily-question&envId=2026-10-11
# Sum of Squares of Special Elements 

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        
        n = len(nums)
        answer = 0

        for i, num in enumerate(nums):
            if n % (i + 1) == 0:
                answer += num ** 2

        return answer