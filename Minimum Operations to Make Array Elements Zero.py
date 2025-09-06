# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/?envType=daily-question&envId=2025-09-06
# Minimum Operations to Make Array Elements Zero

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def _prefix_steps(n: int) -> int:
            if n <= 0:
                return 0
            K = 0
            p = 1  # 4^0
            while p * 4 <= n:
                p *= 4
                K += 1
            K = 0
            p = 1
            total = 0
            while True:
                nxt = p * 4
                if nxt - 1 <= n:
                    total += (K + 1) * (3 * p)
                    p = nxt
                    K += 1
                else:
                    break
            if p <= n:
                total += (K + 1) * (n - p + 1)
            return total

        ans = 0
        for l, r in queries:
            if l > r:
                l, r = r, l
            S = _prefix_steps(r) - _prefix_steps(l - 1)
            ans += (S + 1) // 2
        return ans