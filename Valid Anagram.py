# https://leetcode.com/problems/valid-anagram/description/?envType=daily-question&envId=2023-12-16
# Valid Anagram

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        
#        return sorted(list(s)) == sorted(list(t))

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)