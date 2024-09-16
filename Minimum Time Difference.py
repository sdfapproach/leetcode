# https://leetcode.com/problems/minimum-time-difference/?envType=daily-question&envId=2024-09-16
# Minimum Time Difference

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        def time_to_minutes(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes

        minutes_list = sorted([time_to_minutes(time) for time in timePoints])

        min_diff = float('inf')

        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i - 1])

        min_diff = min(min_diff, 1440 + minutes_list[0] - minutes_list[-1])

        return min_diff