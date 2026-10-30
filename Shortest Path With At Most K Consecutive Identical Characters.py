# https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/?envType=daily-question&envId=2026-10-30
# Shortest Path With At Most K Consecutive Identical Characters

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        dist[0][1] = 0
        heap = [(0, 0, 1)]

        while heap:
            cost, u, count = heapq.heappop(heap)

            if cost > dist[u][count]:
                continue

            if u == n - 1:
                return cost

            for v, w in graph[u]:

                if labels[u] == labels[v]:
                    next_count = count + 1
                else:
                    next_count = 1

                if next_count > k:
                    continue

                next_cost = cost + w

                if next_cost < dist[v][next_count]:
                    dist[v][next_count] = next_cost

                    heapq.heappush(
                        heap,
                        (next_cost, v, next_count)
                    )

        return -1