# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/?envType=daily-question&envId=2025-05-13
# Total Characters in String After Transformations I

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        
        MOD = 10**9 + 7
        
        prev_dp = [1] * 26 
        
        for _ in range(t):
            current_dp = [0] * 26
            for char_code in range(25):
                current_dp[char_code] = prev_dp[char_code + 1]
            
            current_dp[25] = (prev_dp[0] + prev_dp[1]) % MOD
            
            prev_dp = current_dp
            
        total_length = 0

        for char_s in s:
            char_idx = ord(char_s) - ord('a')
            total_length = (total_length + prev_dp[char_idx]) % MOD
            
        return total_length