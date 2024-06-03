# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/?envType=daily-question&envId=2024-06-03
# Append Characters to String to Make Subsequence

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        j = 0
        
        for idx, char in enumerate(s):

            if j < len(t) and char == t[j]:
                j += 1
        
        return len(t) - j