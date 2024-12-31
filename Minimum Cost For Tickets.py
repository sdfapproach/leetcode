# https://leetcode.com/problems/minimum-cost-for-tickets/?envType=daily-question&envId=2024-12-31
# Minimum Cost For Tickets

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        last_day = days[-1]
        dp = [0] * (last_day + 1)
        travel_days = set(days)
        
        for i in range(1, last_day + 1):
            if i not in travel_days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(
                    dp[max(0, i - 1)] + costs[0],
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 30)] + costs[2]
                )
        
        return dp[last_day]