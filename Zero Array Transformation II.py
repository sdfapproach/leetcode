# https://leetcode.com/problems/zero-array-transformation-ii/?envType=daily-question&envId=2025-03-13
# Zero Array Transformation II

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        n = len(nums)
        m = len(queries)
        
        def can_zero(k: int) -> bool:
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r+1] -= val
            total = 0
            for j in range(n):
                total += diff[j]
                if total < nums[j]:
                    return False
            return True
        
        lo, hi = 0, m + 1
        ans = -1
        while lo < hi:
            mid = (lo + hi) // 2
            if can_zero(mid):
                ans = mid
                hi = mid
            else:
                lo = mid + 1
        
        if ans == -1 or ans > m:
            return -1
        return ans