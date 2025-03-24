# https://leetcode.com/problems/count-days-without-meetings/?envType=daily-question&envId=2025-03-24
# Count Days Without Meetings

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        if not meetings:
            return days
        
        meetings.sort(key=lambda x: x[0])
        
        merged = []
        for meeting in meetings:
            if not merged or meeting[0] > merged[-1][1]:
                merged.append(meeting.copy())
            else:
                merged[-1][1] = max(merged[-1][1], meeting[1])
        
        total_meeting_days = 0
        for s, e in merged:
            s_eff = max(s, 1)
            e_eff = min(e, days)
            if s_eff <= e_eff:
                total_meeting_days += (e_eff - s_eff + 1)
        
        available_days = days - total_meeting_days

        return available_days