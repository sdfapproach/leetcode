# https://leetcode.com/problems/count-the-hidden-sequences/?envType=daily-question&envId=2025-04-21
# Count the Hidden Sequences

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        
        x = mi = mx = 0

        for d in differences:
            x += d
            mi = min(mi, x)
            mx = max(mx, x)

        return max(upper - lower - (mx - mi) + 1, 0)