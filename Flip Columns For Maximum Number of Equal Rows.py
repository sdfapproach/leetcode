# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/?envType=daily-question&envId=2024-11-22
# Flip Columns For Maximum Number of Equal Rows

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:

        pattern_count = Counter()
    
        for row in matrix:
            t = tuple(row) if row[0] == 0 else tuple(x ^ 1 for x in row)
            pattern_count[t] += 1

        return max(pattern_count.values())