# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/?envType=daily-question&envId=2026-03-06
# Check if Binary String Has at Most One Segment of Ones

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        flag = False

        for bi in s:
            if bi == "0":
                flag = True
            elif flag == True and bi == "1":
                return False

        return True