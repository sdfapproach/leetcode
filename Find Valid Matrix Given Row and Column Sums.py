# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/?envType=daily-question&envId=2024-07-20
# Find Valid Matrix Given Row and Column Sums

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:

        n, m = len(rowSum), len(colSum)

        result = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                min_val = min(rowSum[i], colSum[j])
                result[i][j] = min_val
                rowSum[i] -= min_val
                colSum[j] -= min_val
        
        return result