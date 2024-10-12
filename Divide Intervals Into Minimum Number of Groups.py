# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/?envType=daily-question&envId=2024-10-12
# Divide Intervals Into Minimum Number of Groups

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        events = []
        for left, right in intervals:
            events.append((left, 1))
            events.append((right + 1, -1))
        
        events.sort()
        
        max_groups = 0
        current_groups = 0
        
        for time, change in events:
            current_groups += change
            max_groups = max(max_groups, current_groups)
        
        return max_groups