# https://leetcode.com/problems/maximum-number-of-items-from-sale-i/?envType=daily-question&envId=2026-11-27
# Maximum Number of Items From Sale I

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        
        min_price = min(price for _, price in items)
        dp = [0] * (budget + 1)

        for factor, price in items:

            count = sum(
                1 for f, _ in items if f % factor == 0
            )

            for b in range(budget, price - 1, -1):
                dp[b] = max(
                    dp[b],
                    dp[b - price] + count
                )

        answer = 0

        for b in range(budget + 1):
            answer = max(
                answer,
                dp[b] + (budget - b) // min_price
            )

        return answer