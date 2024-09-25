# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/?envType=daily-question&envId=2024-09-25
# Sum of Prefix Scores of Strings

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
    
    def get_prefix_score(self, word: str) -> int:
        node = self.root
        score = 0
        for char in word:
            node = node.children[char]
            score += node.count
        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        trie = Trie()

        for word in words:
            trie.insert(word)
        
        answer = []
        for word in words:
            answer.append(trie.get_prefix_score(word))
        
        return answer