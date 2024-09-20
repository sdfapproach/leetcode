# https://leetcode.com/problems/shortest-palindrome/?envType=daily-question&envId=2024-09-20
# Shortest Palindrome

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        def get_kmp_table(s: str):
            n = len(s)
            kmp = [0] * n
            j = 0
            for i in range(1, n):
                while j > 0 and s[i] != s[j]:
                    j = kmp[j - 1]
                if s[i] == s[j]:
                    j += 1
                kmp[i] = j
            return kmp

        if not s:
            return ""
        
        reverse_s = s[::-1]
        
        new_s = s + '#' + reverse_s
        
        kmp_table = get_kmp_table(new_s)
        
        longest_palindrome_len = kmp_table[-1]
        
        to_add = reverse_s[:len(s) - longest_palindrome_len]
        
        return to_add + s