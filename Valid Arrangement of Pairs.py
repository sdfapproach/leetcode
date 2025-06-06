# https://leetcode.com/problems/valid-arrangement-of-pairs/?envType=daily-question&envId=2024-11-30
# Valid Arrangement of Pairs

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        start_node = pairs[0][0]
        for node in graph:
            if out_degree[node] - in_degree[node] == 1:
                start_node = node
                break

        stack = [start_node]
        result = []

        while stack:
            while graph[stack[-1]]:
                next_node = graph[stack[-1]].pop()
                stack.append(next_node)
            result.append(stack.pop())

        result.reverse()

        return [[result[i], result[i+1]] for i in range(len(result) - 1)]