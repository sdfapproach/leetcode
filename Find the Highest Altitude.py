# https://leetcode.com/problems/find-the-highest-altitude/?envType=daily-question&envId=2026-06-19
# Find the Highest Altitude

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        highest = 0
        altitude = 0

        for n in gain:
            altitude += n
            highest = max(highest, altitude)

        return highest