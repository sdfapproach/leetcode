# https://leetcode.com/problems/find-the-original-typed-string-i/?envType=daily-question&envId=2025-07-01
# Find the Original Typed String I

class Solution:
    def possibleStringCount(self, word: str) -> int:

        runs = []
        n = len(word)
        i = 0
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            runs.append(j - i)
            i = j
        
        total = 1
        
        for L in runs:
            if L >= 2:
                total += (L - 1)
        
        return total