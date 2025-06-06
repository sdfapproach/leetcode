# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/?envType=daily-question&envId=2025-06-06
# Using a Robot to Print the Lexicographically Smallest String

class Solution:
    def robotWithString(self, s: str) -> str:
        
        n = len(s)
        min_suffix = [''] * (n + 1)
        min_suffix[n] = '{'
        
        for i in range(n - 1, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])
        
        t = []
        output = []
        i = 0
        
        while i < n or t:
            while t and (i == n or t[-1] <= min_suffix[i]):
                output.append(t.pop())
            
            if i < n:
                t.append(s[i])
                i += 1
        
        return ''.join(output)