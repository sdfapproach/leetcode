# https://leetcode.com/problems/plus-one/?envType=daily-question&envId=2026-01-01
# Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = ""

        for digit in digits:
            s += str(digit)

        s = int(s)
        s += 1
        s = str(s)

        return [int(n) for n in s]