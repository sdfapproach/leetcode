# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/?envType=daily-question&envId=2024-07-26
# Find the City With the Smallest Number of Neighbors at a Threshold Distance

import sys

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        INF = sys.maxsize
        dist = [[INF] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
        
        for edge in edges:
            fromi, toi, weighti = edge
            dist[fromi][toi] = weighti
            dist[toi][fromi] = weighti
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        minReachableCities = n
        resultCity = -1

        for i in range(n):
            reachableCities = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    reachableCities += 1
            
            if reachableCities < minReachableCities or (reachableCities == minReachableCities and i > resultCity):
                minReachableCities = reachableCities
                resultCity = i
        
        return resultCity