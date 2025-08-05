# https://leetcode.com/problems/fruits-into-baskets-ii/?envType=daily-question&envId=2025-08-05
# Fruits Into Baskets II

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        n = len(fruits)

        for fruit in fruits:
            for basket in baskets:
                if fruit <= basket:
                    baskets.remove(basket)
                    n -= 1
                    break

        return n