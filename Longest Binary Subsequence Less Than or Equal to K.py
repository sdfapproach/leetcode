# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/?envType=daily-question&envId=2025-06-26
# Longest Binary Subsequence Less Than or Equal to K

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        
        val = 0
        bit_weight = 1
        ones_cnt = 0
        zeros_cnt = 0
        n = len(s)
        
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                zeros_cnt += 1
                bit_weight = min(bit_weight * 2, k + 1)
            else:
                if val + bit_weight <= k:
                    val += bit_weight
                    ones_cnt += 1
                    bit_weight = min(bit_weight * 2, k + 1)
        
        return zeros_cnt + ones_cnt
