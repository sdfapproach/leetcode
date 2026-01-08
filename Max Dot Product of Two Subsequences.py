# https://leetcode.com/problems/max-dot-product-of-two-subsequences/?envType=daily-question&envId=2026-01-08
# Max Dot Product of Two Subsequences

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        m = len(nums2)
        
        dp = [[float('-inf')] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                curr_product = nums1[i] * nums2[j]
                
                if i > 0 and j > 0:
                    dp[i][j] = max(curr_product, dp[i-1][j-1] + curr_product)
                else:
                    dp[i][j] = curr_product
                
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                    
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
                    
        return dp[n-1][m-1]