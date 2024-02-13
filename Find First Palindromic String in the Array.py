# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/?envType=daily-question&envId=2024-02-13
# Find First Palindromic String in the Array

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        # for word in words:
        #     if word == "".join(reversed(word)):
        #         return word
        
        # return ""

        return next((word for word in words if word == word[::-1]), "")