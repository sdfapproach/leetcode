# https://leetcode.com/problems/create-grid-with-exactly-one-path/?envType=daily-question&envId=2026-10-27
# Create Grid With Exactly One Path

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        
        grid = []

        for i in range(m):
            if i == 0:
                grid.append("." * n)
            else:
                grid.append("#" * (n - 1) + ".")

        return grid