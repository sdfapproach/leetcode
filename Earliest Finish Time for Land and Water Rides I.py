# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/?envType=daily-question&envId=2026-06-02
# Earliest Finish Time for Land and Water Rides I

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        ans = float('inf')

        for i in range(len(landStartTime)):
            land_end = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                finish = max(land_end, waterStartTime[j]) + waterDuration[j]
                ans = min(ans, finish)

        for j in range(len(waterStartTime)):
            water_end = waterStartTime[j] + waterDuration[j]

            for i in range(len(landStartTime)):
                finish = max(water_end, landStartTime[i]) + landDuration[i]
                ans = min(ans, finish)

        return ans