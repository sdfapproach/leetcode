# https://leetcode.com/problems/maximum-matrix-sum/?envType=daily-question&envId=2024-11-24
# Maximum Matrix Sum

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        n = len(matrix)
        total_sum = 0
        min_abs_value = float('inf')
        negative_count = 0

        for i in range(n):
            for j in range(n):
                value = matrix[i][j]
                total_sum += abs(value)
                min_abs_value = min(min_abs_value, abs(value))
                if value < 0:
                    negative_count += 1

        if negative_count % 2 != 0:
            total_sum -= 2 * min_abs_value

        return total_sum