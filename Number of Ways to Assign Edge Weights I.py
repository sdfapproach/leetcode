# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/?envType=daily-question&envId=2026-06-11
# Number of Ways to Assign Edge Weights I

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        
        MOD = 10**9 + 7

        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        q = deque([(1, 0)])
        visited = set([1])
        max_depth = 0

        while q:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)

            for nxt in graph[node]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, depth + 1))

        return pow(2, max_depth - 1, MOD)