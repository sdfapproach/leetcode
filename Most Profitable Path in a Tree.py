# https://leetcode.com/problems/most-profitable-path-in-a-tree/?envType=daily-question&envId=2025-02-24
# Most Profitable Path in a Tree

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        n = len(amount)
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        
        parent = [-1] * n
        depth = [0] * n
        
        def dfs(node: int, par: int, d: int):
            parent[node] = par
            depth[node] = d
            for nxt in tree[node]:
                if nxt == par:
                    continue
                dfs(nxt, node, d + 1)
        
        dfs(0, -1, 0)
        
        bobTime = [math.inf] * n
        t = 0
        node = bob
        while node != -1:
            bobTime[node] = t
            t += 1
            node = parent[node]
        
        maxProfit = -math.inf
        
        def dfsAlice(node: int, par: int, t: int, profit: int):
            if t < bobTime[node]:
                profit += amount[node]
            elif t == bobTime[node]:
                profit += amount[node] // 2
            
            if len(tree[node]) == 1 and node != 0 or (node == 0 and len(tree[node]) == 0):
                nonlocal maxProfit
                maxProfit = max(maxProfit, profit)
                return
            
            for nxt in tree[node]:
                if nxt == par:
                    continue
                dfsAlice(nxt, node, t + 1, profit)
        
        dfsAlice(0, -1, 0, 0)
        return maxProfit