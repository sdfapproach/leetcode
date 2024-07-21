# https://leetcode.com/problems/build-a-matrix-with-conditions/?envType=daily-question&envId=2024-07-21
# Build a Matrix With Conditions

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        
        def topological_sort(conditions, k):
            graph = defaultdict(list)
            in_degree = [0] * (k + 1)
            
            for u, v in conditions:
                graph[u].append(v)
                in_degree[v] += 1
            
            queue = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
            order = []
            
            while queue:
                node = queue.popleft()
                order.append(node)
                
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        queue.append(neighbor)
            
            return order if len(order) == k else []
        
        row_order = topological_sort(rowConditions, k)
        col_order = topological_sort(colConditions, k)
        
        if not row_order or not col_order:
            return []
        
        row_position = {num: i for i, num in enumerate(row_order)}
        col_position = {num: i for i, num in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            row = row_position[num]
            col = col_position[num]
            matrix[row][col] = num
        
        return matrix
