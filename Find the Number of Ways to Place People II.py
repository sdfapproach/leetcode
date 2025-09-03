# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/?envType=daily-question&envId=2025-09-03
# Find the Number of Ways to Place People II

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        
        ans = 0

        points.sort(key=lambda x: (x[0], -x[1]))

        for i, (_, yi) in enumerate(points):
            maxY = -math.inf
            for j in range(i + 1, len(points)):
                _, yj = points[j]
                if yi >= yj > maxY:
                    ans += 1
                    maxY = yj

        return ans