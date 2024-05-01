# https://leetcode.com/problems/reverse-prefix-of-word/?envType=daily-question&envId=2024-05-01
# Reverse Prefix of Word

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        return "".join(reversed(word[0:word.find(ch)+1])) + word[word.find(ch)+1:]