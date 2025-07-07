# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/?envType=daily-question&envId=2025-07-07
# Maximum Number of Events That Can Be Attended

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        events.sort(key=lambda x: x[0])
        n = len(events)
        event_heap = []
        i = 0
        day = 0
        attended = 0

        while i < n or event_heap:
            if not event_heap:
                day = max(day, events[i][0])

            while i < n and events[i][0] <= day:
                heapq.heappush(event_heap, events[i][1])
                i += 1

            while event_heap and event_heap[0] < day:
                heapq.heappop(event_heap)

            if event_heap:
                heapq.heappop(event_heap)
                attended += 1
                day += 1

        return attended