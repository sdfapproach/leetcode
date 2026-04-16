# https://leetcode.com/problems/closest-equal-element-queries/?envType=daily-question&envId=2026-04-16
# Closest Equal Element Queries

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        n = len(nums)
        
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)
        
        res = []
        
        for q in queries:
            val = nums[q]
            indices = pos[val]
            
            if len(indices) == 1:
                res.append(-1)
                continue
            
            import bisect

            i = bisect.bisect_left(indices, q)
            
            left = indices[i - 1] if i > 0 else indices[-1]
            right = indices[i + 1] if i < len(indices) - 1 else indices[0]
            
            d1 = abs(q - left)
            d2 = abs(q - right)
            
            d1 = min(d1, n - d1)
            d2 = min(d2, n - d2)
            
            res.append(min(d1, d2))
        
        return res