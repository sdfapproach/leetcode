# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/?envType=daily-question&envId=2026-06-12
# Number of Ways to Assign Edge Weights II

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        MOD = 10**9 + 7

        n = len(edges) + 1
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        LOG = (n + 1).bit_length()
        parent = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        q = deque([1])
        visited = [False] * (n + 1)
        visited[1] = True

        while q:
            node = q.popleft()

            for nxt in graph[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    parent[0][nxt] = node
                    depth[nxt] = depth[node] + 1
                    q.append(nxt)

        for p in range(1, LOG):
            for node in range(1, n + 1):
                parent[p][node] = parent[p - 1][parent[p - 1][node]]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]

            for p in range(LOG):
                if diff & (1 << p):
                    a = parent[p][a]

            if a == b:
                return a

            for p in range(LOG - 1, -1, -1):
                if parent[p][a] != parent[p][b]:
                    a = parent[p][a]
                    b = parent[p][b]

            return parent[0][a]

        ans = []

        for u, v in queries:
            w = lca(u, v)
            d = depth[u] + depth[v] - 2 * depth[w]

            if d == 0:
                ans.append(0)
            else:
                ans.append(pow(2, d - 1, MOD))

        return ans