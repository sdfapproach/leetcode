# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/?envType=daily-question&envId=2026-06-01
# Minimum Cost of Buying Candies With Discount

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        cost.sort(reverse=True)

        min_cost = 0

        for i, n in enumerate(cost):
            if i % 3 != 2:
                min_cost += n

        return min_cost