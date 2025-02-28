# https://leetcode.com/problems/shortest-common-supersequence/?envType=daily-question&envId=2025-02-28
# Shortest Common Supersequence 

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        m, n = len(str1), len(str2)
        dp = [["" for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = dp[i][j] + str1[i]
                else:
                    if len(dp[i+1][j]) >= len(dp[i][j+1]):
                        dp[i+1][j+1] = dp[i+1][j]
                    else:
                        dp[i+1][j+1] = dp[i][j+1]
                        
        lcs = dp[m][n]
        
        i = j = 0
        ans = []
        for c in lcs:
            while i < len(str1) and str1[i] != c:
                ans.append(str1[i])
                i += 1
            while j < len(str2) and str2[j] != c:
                ans.append(str2[j])
                j += 1
            ans.append(c)
            i += 1
            j += 1
        
        ans.append(str1[i:])
        ans.append(str2[j:])
        
        return "".join(ans)