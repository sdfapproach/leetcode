# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/?envType=daily-question&envId=2025-12-17
# Best Time to Buy and Sell Stock V

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        
        n = len(prices)
        if n < 2 or k == 0:
            return 0

        k = min(k, n // 2)

        prev_dp = [0] * n
        
        for t in range(1, k + 1):
            curr_dp = [0] * n
            m_low = -prices[0]
            m_high = prices[0]
            
            for i in range(1, n):
                curr_dp[i] = max(curr_dp[i-1], prices[i] + m_low, -prices[i] + m_high)
                
                if i < n - 1:
                    m_low = max(m_low, prev_dp[i-1] - prices[i])
                    m_high = max(m_high, prev_dp[i-1] + prices[i])
            
            prev_dp = curr_dp
            
        return prev_dp[-1]