# https://leetcode.com/problems/rotated-digits/?envType=daily-question&envId=2026-05-02
# Rotated Digits

class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        good = {2, 5, 6, 9}
        invalid = {3, 4, 7}
        
        count = 0
        
        for num in range(1, n + 1):
            s = str(num)
            
            if any(c in '347' for c in s):
                continue
            
            if any(int(c) in good for c in s):
                count += 1
        
        return count