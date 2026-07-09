# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/?envType=daily-question&envId=2026-07-09
# Path Existence Queries in a Graph I

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        
        group = [0] * n
        comp = 0

        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                comp += 1
            group[i] = comp

        ans = []

        for u, v in queries:
            ans.append(group[u] == group[v])

        return ans