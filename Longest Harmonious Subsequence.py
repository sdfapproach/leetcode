# https://leetcode.com/problems/longest-harmonious-subsequence/?envType=daily-question&envId=2025-06-30
# Longest Harmonious Subsequence

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        freq = Counter(nums)
        best = 0

        for x in freq:
            if x + 1 in freq:
                best = max(best, freq[x] + freq[x+1])
        return best