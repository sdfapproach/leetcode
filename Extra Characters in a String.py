# https://leetcode.com/problems/extra-characters-in-a-string/?envType=daily-question&envId=2024-09-23
# Extra Characters in a String

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        word_set = set(dictionary)
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            for j in range(i + 1, n + 1):
                if s[i:j] in word_set:
                    dp[i] = min(dp[i], dp[j])
        
        return dp[0]