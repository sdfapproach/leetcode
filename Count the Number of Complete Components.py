# https://leetcode.com/problems/count-the-number-of-complete-components/?envType=daily-question&envId=2025-03-22
# Count the Number of Complete Components

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = [False] * n
        complete_count = 0
        
        def bfs(start: int) -> List[int]:
            queue = deque([start])
            comp = []
            visited[start] = True
            while queue:
                node = queue.popleft()
                comp.append(node)
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            return comp
        
        for i in range(n):
            if not visited[i]:
                comp = bfs(i)
                comp_set = set(comp)
                k = len(comp)
                is_complete = True
                for node in comp:
                    if len(graph[node].intersection(comp_set)) != k - 1:
                        is_complete = False
                        break
                if is_complete:
                    complete_count += 1
        
        return complete_count