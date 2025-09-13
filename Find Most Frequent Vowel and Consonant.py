# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/?envType=daily-question&envId=2025-09-13
# Find Most Frequent Vowel and Consonant

class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        vowel = ('a', 'e', 'i', 'o', 'u')

        v, c = 0, 0

        for char, freq in Counter(s).items():
            if char in vowel:
                v = max(v, freq)
            else:
                c = max(c, freq)

        return v + c