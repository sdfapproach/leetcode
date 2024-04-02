# https://leetcode.com/problems/isomorphic-strings/?envType=daily-question&envId=2024-04-02
# Isomorphic Strings

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mapST = {}
        mapTS = {}

        for i in range(len(s)):
            charS, charT = s[i], t[i]

            if charS in mapST:
                if mapST[charS] != charT:
                    return False
            else:
                mapST[charS] = charT

            if charT in mapTS:
                if mapTS[charT] != charS:
                    return False
            else:
                mapTS[charT] = charS

        return True