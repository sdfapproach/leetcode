# https://leetcode.com/problems/word-subsets/?envType=daily-question&envId=2025-01-10
# Word Subsets

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        max_freq = Counter()

        for word2 in words2:
            freq = Counter(word2)
            for char in freq:
                max_freq[char] = max(max_freq[char], freq[char])
        
        subsets = []

        for word1 in words1:
            freq = Counter(word1)
            if all(freq[char] >= max_freq[char] for char in max_freq):
                subsets.append(word1)
        
        return subsets


                