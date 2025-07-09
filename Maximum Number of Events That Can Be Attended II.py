# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/?envType=daily-question&envId=2025-07-08
# Maximum Number of Events That Can Be Attended II

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        events.sort(key=lambda x: x[0])
        starts = [e[0] for e in events]
        n = len(events)
        
        next_idx = [0] * n
        for i, (_, end, _) in enumerate(events):
            j = bisect.bisect_right(starts, end)
            next_idx[i] = j
        
        @lru_cache(None)
        def dp(i: int, rem: int) -> int:
            if rem == 0 or i == n:
                return 0
            res = dp(i+1, rem)
            val = events[i][2] + dp(next_idx[i], rem-1)
            if val > res:
                res = val
            return res
        
        return dp(0, k)