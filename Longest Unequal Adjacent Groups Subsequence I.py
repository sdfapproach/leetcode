# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/?envType=daily-question&envId=2025-05-15
# Longest Unequal Adjacent Groups Subsequence I

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        n = len(words)
    
        subsequence = []
        
        last_group = -1
        
        for i in range(n):
            if groups[i] != last_group:
                subsequence.append(words[i])
                last_group = groups[i]
        
        return subsequence