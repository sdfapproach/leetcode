# https://leetcode.com/problems/weighted-word-mapping/?envType=daily-question&envId=2026-06-13
# Weighted Word Mapping

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        string = ""

        for word in words:

            c_sum = 0

            for c in word:
                c_sum += weights[(ord(c)-97)]

            string += (chr(abs(122 - (c_sum%26))))

        return string
