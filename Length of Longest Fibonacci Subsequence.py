# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/?envType=daily-question&envId=2025-02-27
# Length of Longest Fibonacci Subsequence

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        n = len(arr)
        index = {x: i for i, x in enumerate(arr)}
        
        dp = [[2] * n for _ in range(n)]
        maxLen = 0
        
        for i in range(n):
            for j in range(i):
                prev = arr[i] - arr[j]
                if prev in index and index[prev] < j:
                    k = index[prev]
                    dp[j][i] = dp[k][j] + 1
                    maxLen = max(maxLen, dp[j][i])
        
        return maxLen if maxLen >= 3 else 0