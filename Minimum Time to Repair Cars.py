# https://leetcode.com/problems/minimum-time-to-repair-cars/submissions/1575840896/?envType=daily-question&envId=2025-03-16
# Minimum Time to Repair Cars

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        lo = 0
        hi = max(ranks) * cars * cars
        ans = hi
        
        while lo <= hi:
            mid = (lo + hi) // 2
            total = 0
            for r in ranks:
                total += int(math.sqrt(mid / r))
            if total >= cars:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans