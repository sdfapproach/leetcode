# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/?envType=daily-question&envId=2025-07-27
# Count Hills and Valleys in an Array

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        collapsed = []
        for x in nums:
            if not collapsed or collapsed[-1] != x:
                collapsed.append(x)
        
        cnt = 0
        m = len(collapsed)
        for i in range(1, m - 1):
            if collapsed[i] > collapsed[i-1] and collapsed[i] > collapsed[i+1]:
                cnt += 1
            elif collapsed[i] < collapsed[i-1] and collapsed[i] < collapsed[i+1]:
                cnt += 1
        
        return cnt