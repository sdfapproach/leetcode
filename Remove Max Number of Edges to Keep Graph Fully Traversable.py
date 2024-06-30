# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/?envType=daily-question&envId=2024-06-30
# Remove Max Number of Edges to Keep Graph Fully Traversable

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
        return True

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        uf_a = UnionFind(n)
        uf_b = UnionFind(n)

        edges = sorted(edges, key=lambda x: -x[0])

        used_edges = 0

        for t, u, v in edges:
            u -= 1
            v -= 1
            if t == 3:
                if uf_a.union(u, v):
                    uf_b.union(u, v)
                    used_edges += 1
            elif t == 1:
                if uf_a.union(u, v):
                    used_edges += 1
            elif t == 2:
                if uf_b.union(u, v):
                    used_edges += 1

        if len(set(uf_a.find(i) for i in range(n))) != 1 or len(set(uf_b.find(i) for i in range(n))) != 1:
            return -1

        return len(edges) - used_edges