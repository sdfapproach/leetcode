# https://leetcode.com/problems/soup-servings/?envType=daily-question&envId=2025-08-08
# Soup Servings

class Solution:
    def soupServings(self, n: int) -> float:
        
        if n >= 4800:  
            return 1.0

        @lru_cache(None)
        def prob(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            return 0.25 * (
                prob(a-100, b) +
                prob(a-75,  b-25) +
                prob(a-50,  b-50) +
                prob(a-25,  b-75)
            )

        return prob(n, n)