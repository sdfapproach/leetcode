# https://leetcode.com/problems/maximum-running-time-of-n-computers/?envType=daily-question&envId=2025-12-01
# Maximum Running Time of N Computers

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        
        left, right = 0, sum(batteries) // n
        
        ans = 0
        
        while left <= right:
            target_time = (left + right) // 2
            
            available_power = 0
            for b in batteries:
                available_power += min(b, target_time)
            
            if available_power >= n * target_time:
                ans = target_time
                left = target_time + 1
            else:
                right = target_time - 1
                
        return ans