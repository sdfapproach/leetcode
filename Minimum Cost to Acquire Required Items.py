# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/?envType=daily-question&envId=2026-11-11
# Minimum Cost to Acquire Required Items

class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
        both = min(need1, need2)

        answer = (
            both * min(costBoth, cost1 + cost2)
            + (need1 - both) * min(cost1, costBoth)
            + (need2 - both) * min(cost2, costBoth)
        )

        return answer