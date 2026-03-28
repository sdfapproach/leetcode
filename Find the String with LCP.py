# https://leetcode.com/problems/find-the-string-with-lcp/?envType=daily-question&envId=2026-03-28
# Find the String with LCP

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        
        n = len(lcp)
        word = [''] * n
        curr_char = 'a'

        for i in range(n):
            if not word[i]:
                if curr_char > 'z':
                    return ""
                
                for j in range(i, n):
                    if lcp[i][j] > 0:
                        word[j] = curr_char
                
                curr_char = chr(ord(curr_char) + 1)

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected_lcp = 0
                if word[i] == word[j]:
                    if i + 1 < n and j + 1 < n:
                        expected_lcp = lcp[i+1][j+1] + 1
                    else:
                        expected_lcp = 1
                
                if lcp[i][j] != expected_lcp:
                    return ""

        return "".join(word)