# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/?envType=daily-question&envId=2025-10-15
# Adjacent Increasing Subarrays Detection II

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 2: 
            return 0

        inc = [1 if nums[i] < nums[i+1] else 0 for i in range(n-1)]
        pref = [0] * (n)
        for i in range(n-1):
            pref[i+1] = pref[i] + inc[i]

        def ok(k: int) -> bool:
            if k == 0:
                return True
            if 2 * k > n:
                return False
            for a in range(0, n - 2*k + 1):
                first = pref[a + k - 1] - pref[a]
                second = pref[a + 2*k - 1] - pref[a + k]
                if first == k - 1 and second == k - 1:
                    return True
            return False

        lo, hi = 0, n // 2
        
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if ok(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo