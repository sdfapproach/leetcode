# https://leetcode.com/problems/longest-palindrome/?envType=daily-question&envId=2024-06-04
# Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        count = Counter(s)
        length = 0
        odd_found = False
        
        for val in count.values():
            if val % 2 == 0:
                length += val
            else:
                length += val - 1
                odd_found = True
        
        if odd_found:
            length += 1
        
        return length