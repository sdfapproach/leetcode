# https://leetcode.com/problems/longest-ideal-subsequence/?envType=daily-question&envId=2024-04-25
# Longest Ideal Subsequence

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        dp = [1] * len(s)
        last_positions = {}

        for i in range(len(s)):
            char_index = ord(s[i])
            for j in range(max(0, char_index - k), char_index + k + 1):
                if j in last_positions:
                    dp[i] = max(dp[i], dp[last_positions[j]] + 1)
            last_positions[char_index] = i

        return max(dp)