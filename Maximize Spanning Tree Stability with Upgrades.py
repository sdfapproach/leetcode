# https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/?envType=daily-question&envId=2026-03-12
# Maximize Spanning Tree Stability with Upgrades

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n
        
    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1
            self.components -= 1
            return True
        return False

class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        must_edges = []
        optional_edges = []
        candidates = set()
        
        dsu_all = DSU(n)
        dsu_must = DSU(n)
        
        for u, v, s, m in edges:
            dsu_all.union(u, v)
            if m == 1:
                must_edges.append((u, v, s))
                candidates.add(s)
                if not dsu_must.union(u, v):
                    return -1 
            else:
                optional_edges.append((u, v, s))
                candidates.add(s)
                candidates.add(2 * s)
                
        if dsu_all.components > 1:
            return -1
            
        candidates = sorted(list(candidates))
        
        def canAchieve(X):
            dsu = DSU(n)
            
            for u, v, s in must_edges:
                if s < X: 
                    return False
                dsu.union(u, v)
                
            for u, v, s in optional_edges:
                if s >= X:
                    dsu.union(u, v)
                    
            upgrades_used = 0
            for u, v, s in optional_edges:
                if s < X and 2 * s >= X:
                    if dsu.find(u) != dsu.find(v):
                        dsu.union(u, v)
                        upgrades_used += 1
                        
            return dsu.components == 1 and upgrades_used <= k

        ans = -1
        low, high = 0, len(candidates) - 1
        
        while low <= high:
            mid = (low + high) // 2
            X = candidates[mid]
            
            if canAchieve(X):
                ans = X
                low = mid + 1
            else:
                high = mid - 1
                
        return ans