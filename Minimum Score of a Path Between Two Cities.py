# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/?envType=daily-question&envId=2026-07-04
# Minimum Score of a Path Between Two Cities

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        graph = defaultdict(list)

        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))

        visited = set([1])
        q = deque([1])
        ans = float('inf')

        while q:
            city = q.popleft()

            for nxt, dist in graph[city]:
                ans = min(ans, dist)

                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        return ans