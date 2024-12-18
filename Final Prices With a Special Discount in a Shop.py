# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/?envType=daily-question&envId=2024-12-18
# Final Prices With a Special Discount in a Shop

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        for i, price in enumerate(prices):

            for next_price in prices[i+1:]:

                if next_price <= price:
                    prices[i] = price-next_price
                    break

        return prices
            