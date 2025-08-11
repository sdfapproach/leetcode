# https://leetcode.com/problems/range-product-queries-of-powers/?envType=daily-question&envId=2025-08-11
# Range Product Queries of Powers

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        MOD = 10**9 + 7
        
        exps = []
        k = 0
        x = n
        while x:
            if x & 1:
                exps.append(k)
            x >>= 1
            k += 1

        pref = [0]
        for e in exps:
            pref.append(pref[-1] + e)

        ans = []
        for l, r in queries:
            s = pref[r + 1] - pref[l]
            ans.append(pow(2, s, MOD))
        return ans