# https://leetcode.com/problems/angle-between-hands-of-a-clock/?envType=daily-question&envId=2026-06-18
# Angle Between Hands of a Clock

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        minute_angle = minutes * 6

        hour_angle = (hour % 12) * 30 + minutes * 0.5

        diff = abs(hour_angle - minute_angle)

        return min(diff, 360 - diff)