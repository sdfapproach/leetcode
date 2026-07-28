# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/?envType=daily-question&envId=2026-07-28
# Smallest Palindromic Rearrangement I

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        
        count = Counter(s)

        left = []
        middle = ""

        for ch in sorted(count):
            left.append(ch * (count[ch] // 2))
            if count[ch] % 2:
                middle = ch

        left = "".join(left)

        return left + middle + left[::-1]