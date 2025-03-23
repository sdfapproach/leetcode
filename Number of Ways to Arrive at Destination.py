# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/?envType=daily-question&envId=2025-03-23
# Number of Ways to Arrive at Destination

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        
        mod = 10**9 + 7
        graph = [[] for _ in range(n)]

        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        heap = [(0, 0)]
        
        while heap:
            d, node = heapq.heappop(heap)
            if d > dist[node]:
                continue
            
            for neighbor, w in graph[node]:
                nd = d + w
                if nd < dist[neighbor]:
                    dist[neighbor] = nd
                    ways[neighbor] = ways[node]
                    heapq.heappush(heap, (nd, neighbor))
                elif nd == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % mod
        
        return ways[n - 1] % mod