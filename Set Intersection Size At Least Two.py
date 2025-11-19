# https://leetcode.com/problems/set-intersection-size-at-least-two/?envType=daily-question&envId=2025-11-20
# Set Intersection Size At Least Two

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: (x[1], -x[0]))
    
        res = []
        
        for start, end in intervals:
            count = 0
            
            if res and res[-1] >= start:
                count += 1
            if len(res) > 1 and res[-2] >= start:
                count += 1
                
            if count == 0:
                res.append(end - 1)
                res.append(end)
            elif count == 1:
                res.append(end)
                
        return len(res)