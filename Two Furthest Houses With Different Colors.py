# https://leetcode.com/problems/two-furthest-houses-with-different-colors/?envType=daily-question&envId=2026-04-20
# Two Furthest Houses With Different Colors

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        n = len(colors)
        ans = 0
        
        for i in range(n - 1, -1, -1):
            if colors[i] != colors[0]:
                ans = max(ans, i)
                break
        
        for i in range(n):
            if colors[i] != colors[n - 1]:
                ans = max(ans, n - 1 - i)
                break
        
        return ans