# https://leetcode.com/problems/path-with-maximum-probability/?envType=daily-question&envId=2024-08-27
# Path with Maximum Probability

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)

        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))

        pq = [(-1, start_node)]
        max_prob = [0] * n
        max_prob[start_node] = 1

        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob
            
            if node == end_node:
                return prob
            
            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > max_prob[neighbor]:
                    max_prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))

        return 0