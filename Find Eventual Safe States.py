# https://leetcode.com/problems/find-eventual-safe-states/?envType=daily-question&envId=2025-01-24
# Find Eventual Safe States

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        reverse_graph = [[] for _ in range(n)]
        indegree = [0] * n

        for node in range(n):
            for neighbor in graph[node]:
                reverse_graph[neighbor].append(node)
                indegree[node] += 1

        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        safe_nodes = []

        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for neighbor in reverse_graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return sorted(safe_nodes)