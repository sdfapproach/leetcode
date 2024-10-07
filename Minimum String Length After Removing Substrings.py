# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/?envType=daily-question&envId=2024-10-07
# Minimum String Length After Removing Substrings

class Solution:
    def minLength(self, s: str) -> int:
        
        # i = 0

        # while i < len(s):

        #     if len(s) > 1 and i > 0 and s[i-1] == "A" and s[i] == "B":
        #         s = s[:i-1] + s[i+1:]
        #         i = 0

        #     if len(s) > 1 and i > 0 and s[i-1] == "C" and s[i] == "D":
        #         s = s[:i-1] + s[i+1:]
        #         i = 0
            
        #     i += 1

        # return len(s)


        i = 1
    
        while i < len(s):
            if s[i-1:i+1] == "AB" or s[i-1:i+1] == "CD":
                s = s[:i-1] + s[i+1:]
                i = max(1, i-1)
            else:
                i += 1

        return len(s)