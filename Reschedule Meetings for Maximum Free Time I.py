# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/?envType=daily-question&envId=2025-07-09
# Reschedule Meetings for Maximum Free Time I

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        
        n = len(startTime)
        G = [0]*(n+1)
        G[0] = startTime[0] - 0
        for i in range(1, n):
            G[i] = startTime[i] - endTime[i-1]
        G[n] = eventTime - endTime[n-1]

        L = min(k+1, n+1)

        curr_sum = sum(G[0:L])
        best = curr_sum

        for start in range(1, (n+1) - L + 1):
            curr_sum += G[start + L - 1]
            curr_sum -= G[start - 1]
            if curr_sum > best:
                best = curr_sum

        return best