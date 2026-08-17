# https://leetcode.com/problems/stone-game-v/?envType=daily-question&envId=2026-08-17
# Stone Game V

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i, x in enumerate(stoneValue):
            prefix[i + 1] = prefix[i] + x

        def range_sum(l, r):
            return prefix[r + 1] - prefix[l]

        dp = [[0] * n for _ in range(n)]

        left_best = [[0] * n for _ in range(n)]

        right_best = [[0] * n for _ in range(n)]

        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                total = range_sum(i, j)

                best = 0

                target = prefix[i] + total // 2

                p = bisect_right(
                    prefix,
                    target,
                    i + 1,
                    j + 1
                ) - 2

                if p >= i:
                    best = max(best, left_best[i][p])

                target = prefix[j + 1] - total // 2

                q = bisect_left(
                    prefix,
                    target,
                    i + 1,
                    j + 1
                )

                if q <= j:
                    best = max(best, right_best[q][j])

                dp[i][j] = best

                left_best[i][j] = max(
                    left_best[i][j - 1],
                    total + dp[i][j]
                )

                right_best[i][j] = max(
                    right_best[i + 1][j],
                    total + dp[i][j]
                )

        return dp[0][n - 1]