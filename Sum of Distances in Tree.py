# https://leetcode.com/problems/sum-of-distances-in-tree/?envType=daily-question&envId=2024-04-28
# Sum of Distances in Tree

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        count = [1] * n
        ans = [0] * n

        def dfs(node, parent):
            for child in tree[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node, parent):
            for child in tree[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + (n - count[child])
                    dfs2(child, node)

        dfs(0, -1)
        dfs2(0, -1)

        return ans