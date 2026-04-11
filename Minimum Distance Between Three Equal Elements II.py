# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/?envType=daily-question&envId=2026-04-11
# Minimum Distance Between Three Equal Elements II

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        
        pos = defaultdict(list)
        
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        ans = float('inf')
        
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            for i in range(len(indices) - 2):
                dist = 2 * (indices[i+2] - indices[i])
                ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1