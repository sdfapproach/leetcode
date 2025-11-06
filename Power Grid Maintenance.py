# https://leetcode.com/problems/power-grid-maintenance/?envType=daily-question&envId=2025-11-06
# Power Grid Maintenance

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        parent = list(range(c + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in connections:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        next_node = [0] * (c + 1)
        comp_min = [0] * (c + 1)
        last = {}

        for node in range(1, c + 1):
            r = find(node)
            if comp_min[r] == 0:
                comp_min[r] = node
            else:
                next_node[last[r]] = node
            last[r] = node

        offline = [False] * (c + 1)

        def update_component_min(r):
            x = comp_min[r]
            while x and offline[x]:
                x = next_node[x]
            comp_min[r] = x if x else 0

        ans = []

        for t, x in queries:
            if t == 1:
                if not offline[x]:
                    ans.append(x)
                else:
                    r = find(x)
                    ans.append(comp_min[r] if comp_min[r] else -1)
            else:
                if not offline[x]:
                    offline[x] = True
                    r = find(x)
                    if comp_min[r] == x:
                        update_component_min(r)

        return ans