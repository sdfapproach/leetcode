# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/?envType=daily-question&envId=2025-02-07
# Find the Number of Distinct Colors Among the Balls

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        ball_color = {}
        color_count = {}
        result = []

        for x, y in queries:
            if x in ball_color:
                old_color = ball_color[x]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]
            
            ball_color[x] = y
            color_count[y] = color_count.get(y, 0) + 1
            
            result.append(len(color_count))
        
        return result