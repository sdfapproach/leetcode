# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/?envType=daily-question&envId=2024-08-29
# Most Stones Removed with Same Row or Column

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        def dfs(x):
            visited.add(x)
            for y in rows[stones[x][0]]:
                if y not in visited:
                    dfs(y)
            for y in cols[stones[x][1]]:
                if y not in visited:
                    dfs(y)

        rows = defaultdict(list)
        cols = defaultdict(list)

        for i, (x, y) in enumerate(stones):
            rows[x].append(i)
            cols[y].append(i)
        
        visited = set()
        num_components = 0

        for i in range(len(stones)):
            if i not in visited:
                dfs(i)
                num_components += 1
        
        return len(stones) - num_components