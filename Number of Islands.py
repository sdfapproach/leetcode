# https://leetcode.com/problems/number-of-islands/?envType=daily-question&envId=2024-04-19
# Number of Islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # num = 1

        # for i, row in enumerate(grid):
        #     for j, island in enumerate(row):
                
        #         if island == 1:
        #             if (j > 0 and row[j-1] == 0) and (j < len(row)-1 and row[j+1] == 0) and (i > 0 and grid[i-1][j] == 0) and (i < len(grid)-1 and grid[i+1][j] == 0):
        #                 num += 1
                        
        # return num

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == '0' or visited[i][j]:
                return
            visited[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        num_islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    num_islands += 1

        return num_islands