# https://leetcode.com/problems/count-the-number-of-special-characters-ii/?envType=daily-question&envId=2026-05-27
# Count the Number of Special Characters II

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        lower_last = {}
        upper_first = {}

        for i, ch in enumerate(word):
            if ch.islower():
                lower_last[ch] = i
            else:
                c = ch.lower()
                if c not in upper_first:
                    upper_first[c] = i

        ans = 0

        for c in lower_last:
            if c in upper_first:
                if lower_last[c] < upper_first[c]:
                    ans += 1

        return ans