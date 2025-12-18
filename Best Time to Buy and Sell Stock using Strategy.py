# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/?envType=daily-question&envId=2025-12-18
# Best Time to Buy and Sell Stock using Strategy

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        
        n = len(prices)
    
        base_profits = [prices[i] * strategy[i] for i in range(n)]
        total_base_profit = sum(base_profits)
        
        pref_prices = [0] * (n + 1)
        pref_base = [0] * (n + 1)
        
        for i in range(n):
            pref_prices[i + 1] = pref_prices[i] + prices[i]
            pref_base[i + 1] = pref_base[i] + base_profits[i]
            
        max_delta = 0
        half_k = k // 2
        
        for i in range(n - k + 1):
            
            new_win_profit = pref_prices[i + k] - pref_prices[i + half_k]
            old_win_profit = pref_base[i + k] - pref_base[i]
            
            delta = new_win_profit - old_win_profit
            if delta > max_delta:
                max_delta = delta
                
        return total_base_profit + max_delta