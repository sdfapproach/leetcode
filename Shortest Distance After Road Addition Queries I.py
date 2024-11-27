# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/?envType=daily-question&envId=2024-11-27
# Shortest Distance After Road Addition Queries I

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)

        for i in range(n - 1):
            graph[i].append((i + 1, 1))
        
        def dijkstra():

            dist = [float('inf')] * n
            dist[0] = 0
            pq = [(0, 0)]

            while pq:
                current_dist, node = heapq.heappop(pq)
                if current_dist > dist[node]:
                    continue
                for neighbor, weight in graph[node]:
                    new_dist = current_dist + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))

            return dist[n - 1] if dist[n - 1] != float('inf') else -1

        result = []

        for u, v in queries:
            graph[u].append((v, 1))
            result.append(dijkstra())

        return result