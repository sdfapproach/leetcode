# https://leetcode.com/problems/two-best-non-overlapping-events/?envType=daily-question&envId=2024-12-08
# Two Best Non-Overlapping Events

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort(key=lambda x: x[1])
    
        max_value = 0
        max_single_event = []
        end_times = []

        for _, end, value in events:
            max_value = max(max_value, value)
            max_single_event.append(max_value)
            end_times.append(end)

        result = 0
        for start, end, value in events:
            idx = bisect_right(end_times, start - 1) - 1
            if idx >= 0:
                result = max(result, value + max_single_event[idx])
            else:
                result = max(result, value)
        
        return result