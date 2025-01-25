# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/?envType=daily-question&envId=2025-01-25
# Make Lexicographically Smallest Array by Swapping Elements

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        n = len(nums)
        uf = UnionFind(n)

        sorted_nums = sorted((value, index) for index, value in enumerate(nums))

        for i in range(n - 1):
            if sorted_nums[i + 1][0] - sorted_nums[i][0] <= limit:
                uf.union(sorted_nums[i][1], sorted_nums[i + 1][1])

        groups = defaultdict(list)

        for i in range(n):
            root = uf.find(i)
            groups[root].append(i)

        result = [0] * n

        for indices in groups.values():
            sorted_indices = sorted(indices)
            sorted_values = sorted(nums[i] for i in indices)
            for index, value in zip(sorted_indices, sorted_values):
                result[index] = value

        return result