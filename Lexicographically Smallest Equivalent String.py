# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/?envType=daily-question&envId=2025-06-05
# Lexicographically Smallest Equivalent String

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent = list(range(26))
        
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x: int, y: int):
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rx < ry:
                parent[ry] = rx
            else:
                parent[rx] = ry
        
        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))
        
        result = []

        for ch in baseStr:
            root = find(ord(ch) - ord('a'))
            result.append(chr(root + ord('a')))
        
        return ''.join(result)