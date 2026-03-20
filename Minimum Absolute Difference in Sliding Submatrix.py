# https://leetcode.com/problems/minimum-absolute-difference-in-sliding-submatrix/?envType=daily-question&envId=2026-03-20
# Minimum Absolute Difference in Sliding Submatrix

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])
        
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                sub_elements = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        sub_elements.append(grid[x][y])
                
                sub_elements.sort()
                
                min_diff = float('inf')
                for t in range(1, len(sub_elements)):
                    if sub_elements[t] != sub_elements[t - 1]:
                        diff = sub_elements[t] - sub_elements[t - 1]
                        if diff < min_diff:
                            min_diff = diff
                
                if min_diff != float('inf'):
                    ans[i][j] = min_diff
                    
        return ans