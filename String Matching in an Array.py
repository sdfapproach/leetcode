# https://leetcode.com/problems/string-matching-in-an-array/?envType=daily-question&envId=2025-01-07
# String Matching in an Array

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        substring = []

        words.sort(key=lambda x:len(x))

        for i, word in enumerate(words):
            for w in words[i+1:]:
                if word in w:
                    substring.append(word)
                    break

        return substring