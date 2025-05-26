# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/?envType=daily-question&envId=2025-05-26
# Largest Color Value in a Directed Graph

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:

        n = len(colors)
        adj = [[] for _ in range(n)]
        in_degree = [0] * n

        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1

        dp = [[0] * 26 for _ in range(n)]
        for i, ch in enumerate(colors):
            dp[i][ord(ch) - ord('a')] = 1

        queue = deque(i for i in range(n) if in_degree[i] == 0)

        visited = 0
        answer = 0

        while queue:
            u = queue.popleft()
            visited += 1
            answer = max(answer, max(dp[u]))

            for v in adj[u]:
                cv = ord(colors[v]) - ord('a')
                for c in range(26):
                    dp[v][c] = max(dp[v][c], dp[u][c] + (1 if c == cv else 0))
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if visited < n:
            return -1

        return answer