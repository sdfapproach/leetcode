# https://leetcode.com/problems/buy-two-chocolates/description/?envType=daily-question&envId=2023-12-20
# Buy Two Chocolates

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        leftover = money
        prices = sorted(prices)
        
        leftover -= prices[0]
        leftover -= prices[1]

        if leftover >= 0:
            return leftover
        else:
            return money