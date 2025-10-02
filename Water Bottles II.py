# https://leetcode.com/problems/water-bottles-ii/?envType=daily-question&envId=2025-10-02
# Water Bottles II

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        full = numBottles
        cost = numExchange
        empty = 0
        drank = 0

        while True:
            if full:
                drank += full
                empty += full
                full = 0
            if empty >= cost:
                empty -= cost
                cost += 1
                full += 1
            else:
                break
        return drank