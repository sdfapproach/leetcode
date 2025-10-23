# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/?envType=daily-question&envId=2025-10-23
# Check If Digits Are Equal in String After Operations I

class Solution(object):
    def hasSameDigits(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        while len(s) > 2:

            st = ""

            for i in range(1, len(s)):
                st += str((int(s[i-1]) + int(s[i])) % 10)

            s = st

        if s[0] == s[1]:
            return True
        else:
            return False