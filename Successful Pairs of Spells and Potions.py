# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/?envType=daily-question&envId=2025-10-08
# Successful Pairs of Spells and Potions

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        potions.sort()
        m = len(potions)
        res = []

        for s in spells:
            need = (success + s - 1) // s
            idx = bisect_left(potions, need)
            res.append(m - idx)
        return res