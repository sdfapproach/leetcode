# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/?envType=daily-question&envId=2025-12-15
# Number of Smooth Descent Periods of a Stock

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        
        if not prices:
            return 0

        total_periods = 1
        
        current_length = 1

        for i in range(1, len(prices)):
            if prices[i] == prices[i-1] - 1:
                current_length += 1
            else:
                current_length = 1
            
            total_periods += current_length
            
        return total_periods