# https://leetcode.com/problems/maximum-69-number/?envType=daily-question&envId=2025-08-16
# Maximum 69 Number

class Solution:
    def maximum69Number (self, num: int) -> int:
        
        s = list(str(num))

        for i, ch in enumerate(s):
            if ch == '6':
                s[i] = '9'
                break

        return int("".join(s))