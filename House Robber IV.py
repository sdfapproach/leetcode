# https://leetcode.com/problems/house-robber-iv/?envType=daily-question&envId=2025-03-15
# House Robber IV

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        
        def canRob(cap: int) -> bool:
            count = 0
            i = 0
            n = len(nums)
            while i < n:
                if nums[i] <= cap:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= k
        
        lo, hi = min(nums), max(nums)
        ans = hi
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if canRob(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans