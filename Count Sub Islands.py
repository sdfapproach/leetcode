# https://leetcode.com/problems/count-sub-islands/?envType=daily-question&envId=2024-08-28
# Count Sub Islands

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def dfs(i, j):

            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] == 0:
                return True

            grid2[i][j] = 0
            is_sub_island = True

            if grid1[i][j] == 0:
                is_sub_island = False
            
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)
            
            return is_sub_island and up and down and left and right
        
        count = 0

        for i in range(len(grid2)):

            for j in range(len(grid2[0])):

                if grid2[i][j] == 1:
                    if dfs(i, j):
                        count += 1
        return count