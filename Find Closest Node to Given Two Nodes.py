# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/?envType=daily-question&envId=2025-05-30
# Find Closest Node to Given Two Nodes

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        n = len(edges)
    
        def compute_dist(start: int) -> list[int]:
            dist = [-1] * n
            cur = start
            d = 0
            while cur != -1 and dist[cur] == -1:
                dist[cur] = d
                d += 1
                cur = edges[cur]
            return dist
        
        dist1 = compute_dist(node1)
        dist2 = compute_dist(node2)
        
        best_node = -1
        best_dist = float('inf')

        for i in range(n):
            d1, d2 = dist1[i], dist2[i]
            if d1 != -1 and d2 != -1:
                d = max(d1, d2)
                if d < best_dist:
                    best_dist = d
                    best_node = i
        
        return best_node