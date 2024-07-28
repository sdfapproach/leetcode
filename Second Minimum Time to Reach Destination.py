# https://leetcode.com/problems/second-minimum-time-to-reach-destination/?envType=daily-question&envId=2024-07-28
# Second Minimum Time to Reach Destination

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        times = [[float('inf'), float('inf')] for _ in range(n+1)]
        times[1][0] = 0
        
        pq = [(0, 1)]
        
        while pq:
            cur_time, node = heapq.heappop(pq)
            
            if node == n and times[n][1] != float('inf'):
                return times[n][1]
            
            for neighbor in graph[node]:
                wait = 0
                if (cur_time // change) % 2 == 1:
                    wait = change - (cur_time % change)
                new_time = cur_time + wait + time
                
                if new_time < times[neighbor][0]:
                    times[neighbor][1] = times[neighbor][0]
                    times[neighbor][0] = new_time
                    heapq.heappush(pq, (new_time, neighbor))
                elif times[neighbor][0] < new_time < times[neighbor][1]:
                    times[neighbor][1] = new_time
                    heapq.heappush(pq, (new_time, neighbor))
        
        return -1