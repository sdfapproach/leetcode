# https://leetcode.com/problems/remove-covered-intervals/?envType=daily-question&envId=2026-07-06
# Remove Covered Intervals

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: (x[0], -x[1]))

        ans = 0
        max_end = 0

        for start, end in intervals:
            if end > max_end:
                ans += 1
                max_end = end

        return ans