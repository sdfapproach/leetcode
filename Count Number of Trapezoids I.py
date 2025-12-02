# https://leetcode.com/problems/count-number-of-trapezoids-i/?envType=daily-question&envId=2025-12-02
# Count Number of Trapezoids I

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        
        MOD = 10**9 + 7

        from collections import defaultdict

        ycount = defaultdict(int)

        for x, y in points:
            ycount[y] += 1

        a_vals = []

        for cnt in ycount.values():
            if cnt >= 2:
                a = cnt * (cnt - 1) // 2
                a_vals.append(a % MOD)

        if len(a_vals) < 2:
            return 0

        sumA = sum(a_vals) % MOD
        sumA2 = sum((a * a) % MOD for a in a_vals) % MOD

        res = (sumA * sumA - sumA2) % MOD
        res = (res * pow(2, MOD - 2, MOD)) % MOD

        return res