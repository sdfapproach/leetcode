# https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/?envType=daily-question&envId=2026-03-13
# Minimum Number of Seconds to Make Mountain Height Zero

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        
        def can(T):
            total = 0
            for t in workerTimes:
                x = int((math.sqrt(1 + 8*T/t) - 1) // 2)
                total += x
                if total >= mountainHeight:
                    return True
            return False
        
        left, right = 0, max(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        
        while left < right:
            mid = (left + right) // 2
            
            if can(mid):
                right = mid
            else:
                left = mid + 1
        
        return left