# https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/?envType=daily-question&envId=2025-12-16
# Maximum Profit from Trading Stocks with Discounts

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        
        adj = defaultdict(list)
        for u, v in hierarchy:
            adj[u].append(v)

        def dfs(u):
            group_buy = {0: 0}       
            group_not_buy = {0: 0}

            for v in adj[u]:
                child_res_0, child_res_1 = dfs(v)
                
                new_group_buy = defaultdict(int)
                for c1, p1 in group_buy.items():
                    for c2, p2 in child_res_1.items():
                        if c1 + c2 <= budget:
                            new_group_buy[c1 + c2] = max(new_group_buy[c1 + c2], p1 + p2)
                group_buy = new_group_buy

                new_group_not_buy = defaultdict(int)
                for c1, p1 in group_not_buy.items():
                    for c2, p2 in child_res_0.items():
                        if c1 + c2 <= budget:
                            new_group_not_buy[c1 + c2] = max(new_group_not_buy[c1 + c2], p1 + p2)
                group_not_buy = new_group_not_buy

            price_full = present[u-1]
            price_half = price_full // 2
            profit_full = future[u-1] - price_full
            profit_half = future[u-1] - price_half

            res_0 = group_not_buy.copy()
            
            for cost, profit in group_buy.items():
                new_cost = cost + price_full
                new_profit = profit + profit_full
                if new_cost <= budget:
                    res_0[new_cost] = max(res_0.get(new_cost, -float('inf')), new_profit)

            res_1 = group_not_buy.copy()
            
            for cost, profit in group_buy.items():
                new_cost = cost + price_half
                new_profit = profit + profit_half
                if new_cost <= budget:
                    res_1[new_cost] = max(res_1.get(new_cost, -float('inf')), new_profit)
            
            return res_0, res_1

        root_dp, _ = dfs(1)
        
        return max(root_dp.values())