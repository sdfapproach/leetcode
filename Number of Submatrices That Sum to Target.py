# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/?envType=daily-question&envId=2024-01-28
# Number of Submatrices That Sum to Target

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        y = len(matrix)
        x = len(matrix[0])
        count = 0

        for row in matrix:
            for i in range(1, x):
                row[i] += row[i - 1]

        for start_col in range(x):
            for end_col in range(start_col, x):
                sums = {0: 1}
                curr_sum = 0
                for row in range(y):
                    curr_sum += matrix[row][end_col] - (matrix[row][start_col - 1] if start_col > 0 else 0)
                    count += sums.get(curr_sum - target, 0)
                    sums[curr_sum] = sums.get(curr_sum, 0) + 1

        return count