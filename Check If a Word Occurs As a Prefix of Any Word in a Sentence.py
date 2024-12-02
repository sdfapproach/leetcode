# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/?envType=daily-question&envId=2024-12-02
# Check If a Word Occurs As a Prefix of Any Word in a Sentence

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        arr = sentence.split(" ")

        for i, word in enumerate(arr):

            if word[:len(searchWord)] == searchWord:
                return i+1

        return -1