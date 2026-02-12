# https://leetcode.com/problems/longest-balanced-substring-i/?envType=daily-question&envId=2026-02-12
# Longest Balanced Substring I

class Solution:
    def longestBalanced(self, s: str) -> int:
        
        n = len(s)
        ans = 0

        for l in range(n):
            freq = defaultdict(int)
            distinct = 0
            max_freq = 0

            for r in range(l, n):
                if freq[s[r]] == 0:
                    distinct += 1
                freq[s[r]] += 1
                max_freq = max(max_freq, freq[s[r]])

                length = r - l + 1

                if length == distinct * max_freq:
                    ans = max(ans, length)

        return ans