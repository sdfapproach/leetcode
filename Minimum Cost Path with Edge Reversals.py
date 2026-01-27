# https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/?envType=daily-question&envId=2026-01-27
# Minimum Cost Path with Edge Reversals

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        
        adj = [[] for _ in range(n)]
        incoming = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))
            incoming[v].append((u, w))

        INF = 10**18
        dist = [[INF, INF] for _ in range(n)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]

        while pq:
            cost, u, used = heapq.heappop(pq)
            if cost > dist[u][used]:
                continue

            for v, w in adj[u]:
                if cost + w < dist[v][0]:
                    dist[v][0] = cost + w
                    heapq.heappush(pq, (cost + w, v, 0))

            if used == 0:
                for v, w in incoming[u]:
                    if cost + 2 * w < dist[v][0]:
                        dist[v][0] = cost + 2 * w
                        heapq.heappush(pq, (cost + 2 * w, v, 0))

        ans = min(dist[n - 1][0], dist[n - 1][1])

        return ans if ans < INF else -1