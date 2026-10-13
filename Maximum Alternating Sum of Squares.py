# https://leetcode.com/problems/maximum-alternating-sum-of-squares/?envType=daily-question&envId=2026-10-13
# Maximum Alternating Sum of Squares

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        squares = sorted(x * x for x in nums)

        n = len(nums)
        negative_count = n // 2

        return (
            sum(squares[negative_count:])
            - sum(squares[:negative_count])
        )