# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/submissions/1984618823/?envType=daily-question&envId=2026-04-21
# Minimize Hamming Distance After Swap Operations

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        
        parent = list(range(len(source)))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa
        
        for a, b in allowedSwaps:
            union(a, b)
        
        groups = defaultdict(list)
        for i in range(len(source)):
            groups[find(i)].append(i)
        
        ans = 0
        
        for indices in groups.values():
            count = Counter()
            
            for i in indices:
                count[source[i]] += 1
            
            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1
                else:
                    ans += 1
        
        return ans