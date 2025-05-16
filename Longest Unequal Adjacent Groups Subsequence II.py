# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/?envType=daily-question&envId=2025-05-16
# Longest Unequal Adjacent Groups Subsequence II

def hamming_distance(word1, word2):
    if len(word1) != len(word2):
        return False
    return sum(1 for x, y in zip(word1, word2) if x != y) == 1

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        n = len(words)
    
        dp = [[] for _ in range(n)]
        
        for i in range(n):
            dp[i].append(words[i])
            for j in range(i):
                if groups[i] != groups[j] and hamming_distance(words[i], words[j]):
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [words[i]]
        
        result = max(dp, key=len)
        
        return result