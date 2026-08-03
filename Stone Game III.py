# https://leetcode.com/problems/stone-game-iii/?envType=daily-question&envId=2026-08-03
# Stone Game III

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            take_sum = 0
            dp[i] = float('-inf')

            for count in range(1, 4):
                if i + count > n:
                    break

                take_sum += stoneValue[i + count - 1]
                dp[i] = max(dp[i], take_sum - dp[i + count])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"