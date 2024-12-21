# https://leetcode.com/problems/maximum-number-of-k-divisible-components/?envType=daily-question&envId=2024-12-21
# Maximum Number of K-Divisible Components

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:

        def dfs(i: int, fa: int):
            s = values[i]
            for j in g[i]:
                if j != fa:
                    s += dfs(j, i)
            nonlocal ans
            ans += s % k == 0
            return s

        g = [[] for _ in range(n)]

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        ans = 0
        dfs(0, -1)

        return ans