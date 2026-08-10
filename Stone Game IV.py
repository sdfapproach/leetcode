# https://leetcode.com/problems/stone-game-iv/?envType=daily-question&envId=2026-08-10
# Stone Game IV

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        dp = [False] * (n + 1)

        for stones in range(1, n + 1):
            square = 1

            while square * square <= stones:
                if not dp[stones - square * square]:
                    dp[stones] = True
                    break

                square += 1

        return dp[n]