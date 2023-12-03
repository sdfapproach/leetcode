# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
# 1662. Check If Two String Arrays are Equivalent

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # self.word1 = word1
        # self.word2 = word2

        # firstWord = ""
        # secondWord = ""
        
        # for word in word1:
        #     firstWord += word

        # for word in word2:
        #     secondWord += word

        # if(firstWord == secondWord):
        #     return True
        # else:
        #     return False

        return ''.join(word1) == ''.join(word2)
