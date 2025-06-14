# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/?envType=daily-question&envId=2025-06-14
# Maximum Difference by Remapping a Digit

class Solution:
    def minMaxDifference(self, num: int) -> int:
        
        s = str(num)
        max_val = float('-inf')
        min_val = float('inf')
        
        for d1 in '0123456789':
            for d2 in '0123456789':
                t = s.replace(d1, d2)
                val = int(t)
                max_val = max(max_val, val)
                min_val = min(min_val, val)
        
        return max_val - min_val
