# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/?envType=daily-question&envId=2026-01-16
# Maximum Square Area by Removing Fences From a Field

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        
        MOD = 10**9 + 7

        hs = sorted([1, m] + hFences)
        vs = sorted([1, n] + vFences)

        def all_diffs(arr: List[int]) -> set[int]:
            diffs = set()
            L = len(arr)
            for i in range(L):
                ai = arr[i]
                for j in range(i + 1, L):
                    diffs.add(arr[j] - ai)
            return diffs

        hdiff = all_diffs(hs)

        best = 0
        Lv = len(vs)

        for i in range(Lv):
            vi = vs[i]
            for j in range(i + 1, Lv):
                d = vs[j] - vi
                if d in hdiff and d > best:
                    best = d

        if best == 0:
            return -1
        return (best * best) % MOD