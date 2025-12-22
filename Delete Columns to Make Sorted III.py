# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/?envType=daily-question&envId=2025-12-22
# Delete Columns to Make Sorted III

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        n = len(strs)
        m = len(strs[0])
        
        dp = [1] * m
        
        for i in range(m):
            for j in range(i):
                is_valid = True
                for k in range(n):
                    if strs[k][j] > strs[k][i]:
                        is_valid = False
                        break
                
                if is_valid:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        max_kept = max(dp)

        return m - max_kept