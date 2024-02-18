# https://leetcode.com/problems/meeting-rooms-iii/?envType=daily-question&envId=2024-02-18
# Meeting Rooms III

from heapq import heappush, heappop

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:

        meetings.sort(key=lambda x: x[0])
    
        free_rooms = [(i, 0) for i in range(n)]
        ongoing_meetings = []
        
        room_usage_count = [0] * n
        
        for start, end in meetings:
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                _, room = heappop(ongoing_meetings)
                heappush(free_rooms, (room, start))
            
            if free_rooms and free_rooms[0][1] <= start:
                room, _ = heappop(free_rooms)
                room_usage_count[room] += 1
                heappush(ongoing_meetings, (end, room))
            else:
                earliest_end, room = heappop(ongoing_meetings)
                room_usage_count[room] += 1
                new_end = max(earliest_end, start) + (end - start)
                heappush(ongoing_meetings, (new_end, room))

        max_meetings = max(room_usage_count)
        return room_usage_count.index(max_meetings)