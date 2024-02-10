# https://leetcode.com/problems/palindromic-substrings/?envType=daily-question&envId=2024-02-10
# Palindromic Substrings

class Solution:
    def countSubstrings(self, s: str) -> int:

        # def palindrome(strn):
        #     return strn == "".join(reversed(strn))
        
        # substrings = []

        # for start in range(len(s)):
        #     for end in range(start + 1, len(s) + 1):
        #         sub_str = s[start:end]
        #         if palindrome(sub_str):
        #             substrings.append(sub_str)

        # return len(substrings)

        def countPalindromesAroundCenter(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        totalPalindromes = 0
        for i in range(len(s)):
            totalPalindromes += countPalindromesAroundCenter(i, i)
            totalPalindromes += countPalindromesAroundCenter(i, i + 1)

        return totalPalindromes