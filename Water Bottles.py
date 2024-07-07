# https://leetcode.com/problems/water-bottles/?envType=daily-question&envId=2024-07-07
# Water Bottles

class Solution:
    
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        drink = 0
        empty = 0

        while numBottles > 0:
            
            drink += numBottles
            empty += numBottles

            numBottles = empty // numExchange
            empty %= numExchange

        return drink