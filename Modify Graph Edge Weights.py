# https://leetcode.com/problems/modify-graph-edge-weights/?envType=daily-question&envId=2024-08-30
# Modify Graph Edge Weights

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:

        def dijkstra(edges: List[List[int]], n: int, source: int, destination: int):
            graph = [[] for _ in range(n)]
            for u, v, w in edges:
                if w != -1:
                    graph[u].append((v, w))
                    graph[v].append((u, w))
            
            dist = [float('inf')] * n
            dist[source] = 0
            pq = [(0, source)]
            
            while pq:
                current_dist, node = heapq.heappop(pq)
                if current_dist > dist[node]:
                    continue
                
                for neighbor, weight in graph[node]:
                    if dist[neighbor] > current_dist + weight:
                        dist[neighbor] = current_dist + weight
                        heapq.heappush(pq, (dist[neighbor], neighbor))
            
            return dist[destination]

        inf = 2 * 10**9
        d = dijkstra(edges, n, source, destination)

        if d < target:
            return []

        ok = d == target

        for e in edges:
            if e[2] > 0:
                continue
            if ok:
                e[2] = inf
                continue
            e[2] = 1
            d = dijkstra(edges, n, source, destination)

            if d <= target:
                ok = True
                e[2] += target - d

        return edges if ok else []