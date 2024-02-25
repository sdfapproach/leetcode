# https://leetcode.com/problems/greatest-common-divisor-traversal/?envType=daily-question&envId=2024-02-25
# Greatest Common Divisor Traversal

def primeFactors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n = n // i
    if n > 2:
        factors.add(n)
    return factors

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        parent = [i for i in range(n)]
        rank = [0] * n
        factorDict = {}

        for i, num in enumerate(nums):
            factors = primeFactors(num)
            for factor in factors:
                if factor not in factorDict:
                    factorDict[factor] = []
                factorDict[factor].append(i)

        for indices in factorDict.values():
            for i in range(len(indices) - 1):
                union(parent, rank, indices[i], indices[i + 1])

        root = find(parent, 0)
        for i in range(1, n):
            if find(parent, i) != root:
                return False

        return True