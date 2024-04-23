# https://leetcode.com/problems/minimum-height-trees/?envType=daily-question&envId=2024-04-23
# Minimum Height Trees

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(set)

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        leaves = deque()
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_size = len(leaves)
            remaining_nodes -= leaves_size
            for _ in range(leaves_size):
                leaf = leaves.popleft()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    leaves.append(neighbor)
        
        return list(leaves)