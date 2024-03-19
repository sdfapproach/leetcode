# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/?envType=daily-question&envId=2024-03-18
# Minimum Number of Arrows to Burst Balloons

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrows = 1
        arrow_position = points[0][1]

        for xstart, xend in points:
            if xstart > arrow_position:
                arrows += 1
                arrow_position = xend

        return arrows