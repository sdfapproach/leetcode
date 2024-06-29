# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/?envType=daily-question&envId=2024-06-29
# All Ancestors of a Node in a Directed Acyclic Graph

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)

        for from_node, to_node in edges:

            graph[to_node].append(from_node)
        
        ancestors = [set() for _ in range(n)]
        
        for node in range(n):

            queue = deque([node])

            while queue:

                current = queue.popleft()

                for parent in graph[current]:

                    if parent not in ancestors[node]:
                        ancestors[node].add(parent)
                        queue.append(parent)
        
        result = [sorted(list(ancestor)) for ancestor in ancestors]
        
        return result