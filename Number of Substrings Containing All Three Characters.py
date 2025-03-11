# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/?envType=daily-question&envId=2025-03-11
# Number of Substrings Containing All Three Characters

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        n = len(s)
        count = [0, 0, 0]
        l = 0
        res = 0
        
        for r in range(n):
            count[ord(s[r]) - ord('a')] += 1
            
            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                res += (n - r)
                count[ord(s[l]) - ord('a')] -= 1
                l += 1
        
        return res