# https://leetcode.com/problems/maximum-path-score-in-a-grid/submissions/1992125900/?envType=daily-question&envId=2026-04-30
# Maximum Path Score in a Grid

class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        
        m, n = len(grid), len(grid[0])

        def score_and_cost(value: int) -> tuple[int, int]:
            if value == 0:
                return 0, 0
            elif value == 1:
                return 1, 1
            else:
                return 2, 1

        NEG = -10**18

        dp = [[[NEG] * (k + 1) for _ in range(n)] for _ in range(m)]

        start_score, start_cost = score_and_cost(grid[0][0])

        if start_cost <= k:
            dp[0][0][start_cost] = start_score

        for i in range(m):
            for j in range(n):
                cell_score, cell_cost = score_and_cost(grid[i][j])

                for cost in range(k + 1):
                    if dp[i][j][cost] == NEG:
                        continue

                    ni, nj = i + 1, j
                    if ni < m:
                        next_score, next_cost = score_and_cost(grid[ni][nj])
                        new_cost = cost + next_cost

                        if new_cost <= k:
                            dp[ni][nj][new_cost] = max(
                                dp[ni][nj][new_cost],
                                dp[i][j][cost] + next_score
                            )

                    ni, nj = i, j + 1
                    if nj < n:
                        next_score, next_cost = score_and_cost(grid[ni][nj])
                        new_cost = cost + next_cost

                        if new_cost <= k:
                            dp[ni][nj][new_cost] = max(
                                dp[ni][nj][new_cost],
                                dp[i][j][cost] + next_score
                            )

        answer = max(dp[m - 1][n - 1])

        return answer if answer != NEG else -1