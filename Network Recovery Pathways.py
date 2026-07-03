# https://leetcode.com/problems/network-recovery-pathways/?envType=daily-question&envId=2026-07-03
# Network Recovery Pathways

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        
        n = len(online)

        if not edges:
            return -1

        graph = [[] for _ in range(n)]
        indeg = [0] * n

        for u, v, c in edges:
            graph[u].append((v, c))
            indeg[v] += 1

        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)

        topo = []
        while q:
            u = q.popleft()
            topo.append(u)

            for v, _ in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        def can(score):
            INF = float('inf')
            dist = [INF] * n
            dist[0] = 0

            for u in topo:
                if dist[u] == INF:
                    continue

                for v, cost in graph[u]:
                    if cost < score:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    nd = dist[u] + cost
                    if nd < dist[v]:
                        dist[v] = nd

            return dist[n - 1] <= k

        left, right = 0, max(c for _, _, c in edges)
        ans = -1

        while left <= right:
            mid = (left + right) // 2

            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans