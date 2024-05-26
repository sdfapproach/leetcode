# https://leetcode.com/problems/student-attendance-record-ii/?envType=daily-question&envId=2024-05-26
# Student Attendance Record II

class Solution:
    def checkRecord(self, n: int) -> int:
        
        if n == 0:
            return 1

        mod = (10**9 + 7)

        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for A in range(2):
                for L in range(3):
                    dp[i][A][0] = (dp[i][A][0] + dp[i-1][A][L]) % mod
                    if A < 1:
                        dp[i][A+1][0] = (dp[i][A+1][0] + dp[i-1][A][L]) % mod
                    if L < 2:
                        dp[i][A][L+1] = (dp[i][A][L+1] + dp[i-1][A][L]) % mod

        result = 0
        for A in range(2):
            for L in range(3):
                result = (result + dp[n][A][L]) % mod

        return result