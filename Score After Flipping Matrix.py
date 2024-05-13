# https://leetcode.com/problems/score-after-flipping-matrix/?envType=daily-question&envId=2024-05-13
# Score After Flipping Matrix

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:

        # score = 0

        # for i in range(len(grid)):

        #     if grid[i][0] == 0:

        #         for j, row in enumerate(grid[i]):
        #             if row == 0:
        #                 grid[i][j] = 1
        #             else:
        #                 grid[i][j] = 0

        # for i in range(len(grid[0])):

        #     count = 0

        #     for j in range(len(grid)):

        #         if grid[j][i] == 1:
        #             count += 1

        #     if count < len(grid) / 2:

        #         for j in range(len(grid)):

        #             if grid[j][i] == 1:
        #                 grid[j][i] = 0
        #             else:
        #                 grid[j][i] = 1

        # text = "0b"

        # for row in grid:
        #     for n in row:
        #         text += str(n)

        #     score += int(text, 2)
        #     text = "0b"

        # return score

        m, n = len(grid), len(grid[0])
        score = 0

        for i in range(m):
            if grid[i][0] == 0:
                grid[i] = [1 - x for x in grid[i]]

        for j in range(n):
            count = sum(grid[i][j] for i in range(m))
            if count < m / 2:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]

        for row in grid:
            score += int(''.join(map(str, row)), 2)

        return score