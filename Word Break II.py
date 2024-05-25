# https://leetcode.com/problems/word-break-ii/?envType=daily-question&envId=2024-05-25
# Word Break II

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def backtrack(start):
            if start == len(s):
                return [[]]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordDict:
                    for subsentence in backtrack(end):
                        sentences.append([word] + subsentence)

            return sentences

        wordDict = set(wordDict)
        result = backtrack(0)
        return [" ".join(words) for words in result]