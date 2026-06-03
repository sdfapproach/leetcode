# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/?envType=daily-question&envId=2026-06-03
# Earliest Finish Time for Land and Water Rides II

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        land_end  = [s + d for s, d in zip(landStartTime,  landDuration)]
        water_end = [s + d for s, d in zip(waterStartTime, waterDuration)]
    
        min_land_end  = min(land_end)
        min_water_end = min(water_end)
    
        best_lf = min(
            max(min_land_end + wd, we)
            for wd, we in zip(waterDuration, water_end)
        )
    
        best_wf = min(
            max(min_water_end + ld, le)
            for ld, le in zip(landDuration, land_end)
        )
    
        return min(best_lf, best_wf)