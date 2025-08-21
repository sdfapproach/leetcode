# https://leetcode.com/problems/count-submatrices-with-all-ones/?envType=daily-question&envId=2025-08-21
# Count Submatrices With All Ones

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        m, n = len(mat), len(mat[0]) if mat else 0
        if m == 0 or n == 0:
            return 0

        left = [[0]*n for _ in range(m)]
        for i in range(m):
            run = 0
            for j in range(n):
                run = run + 1 if mat[i][j] == 1 else 0
                left[i][j] = run

        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                minw = float('inf')
                for r in range(i, -1, -1):
                    if left[r][j] == 0:
                        break
                    minw = min(minw, left[r][j])
                    ans += minw
        return ans