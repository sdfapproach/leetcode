# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/?envType=daily-question&envId=2026-04-10
# Minimum Distance Between Three Equal Elements I

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
                left = indices[i]
                right = indices[i + 2]
                
                dist = 2 * (right - left)
                ans = min(ans, dist)
        
        return ans if ans != float('inf') else -1