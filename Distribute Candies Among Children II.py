# https://leetcode.com/problems/distribute-candies-among-children-ii/?envType=daily-question&envId=2025-06-01
# Distribute Candies Among Children II

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        def comb2(x: int) -> int:
            if x < 2:
                return 0
            return x * (x - 1) // 2

        S0 = comb2(n + 2)

        M1 = n - (limit + 1)
        S1 = comb2(M1 + 2) if M1 >= 0 else 0

        M2 = n - 2 * (limit + 1)
        S2 = comb2(M2 + 2) if M2 >= 0 else 0

        M3 = n - 3 * (limit + 1)
        S3 = comb2(M3 + 2) if M3 >= 0 else 0

        return S0 - 3 * S1 + 3 * S2 - S3