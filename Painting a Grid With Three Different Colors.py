# https://leetcode.com/problems/painting-a-grid-with-three-different-colors/?envType=daily-question&envId=2025-05-18
# Painting a Grid With Three Different Colors

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        
        MOD = 10**9 + 7
        
        def generate_valid_colorings(m):
            valid_colorings = []
            
            def backtrack(coloring, length):
                if length == m:
                    valid_colorings.append(coloring)
                    return
                
                for color in [1, 2, 3]:
                    if length == 0 or coloring[-1] != color:
                        backtrack(coloring + [color], length + 1)
            
            backtrack([], 0)
            return valid_colorings
        
        def can_be_adjacent(row1, row2):
            for i in range(m):
                if row1[i] == row2[i]:
                    return False
            return True
        
        valid_rows = generate_valid_colorings(m)
        row_count = len(valid_rows)
        
        adjacency = [[False] * row_count for _ in range(row_count)]

        for i in range(row_count):
            for j in range(row_count):
                adjacency[i][j] = can_be_adjacent(valid_rows[i], valid_rows[j])
        
        dp = [[0] * row_count for _ in range(n)]
        
        for j in range(row_count):
            dp[0][j] = 1
        
        for i in range(1, n):
            for j in range(row_count):
                for k in range(row_count):
                    if adjacency[k][j]:
                        dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
        
        return sum(dp[n-1]) % MOD
