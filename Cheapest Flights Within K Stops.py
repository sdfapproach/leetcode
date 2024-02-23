# https://leetcode.com/problems/cheapest-flights-within-k-stops/?envType=daily-question&envId=2024-02-23
# Cheapest Flights Within K Stops

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float('inf')] * n
        costs[src] = 0

        for _ in range(k+1):
            temp_costs = costs.copy()
            for u, v, w in flights:
                if costs[u] != float('inf') and costs[u] + w < temp_costs[v]:
                    temp_costs[v] = costs[u] + w
            costs = temp_costs

        return -1 if costs[dst] == float('inf') else costs[dst]