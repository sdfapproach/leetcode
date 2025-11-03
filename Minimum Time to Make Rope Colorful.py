# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/?envType=daily-question&envId=2025-11-03
# Minimum Time to Make Rope Colorful

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        total_time = 0
        n = len(colors)
        
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                total_time += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])

        return total_time