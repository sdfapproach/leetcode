# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/?envType=daily-question&envId=2025-01-04
# Unique Length-3 Palindromic Subsequences

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        
        result = set()
    
        first = {}
        last = {}
        
        for i, char in enumerate(s):
            if char not in first:
                first[char] = i
            last[char] = i
        
        for char in first:
            if first[char] < last[char]:
                for middle in set(s[first[char] + 1:last[char]]):
                    result.add(char + middle + char)
        
        return len(result)