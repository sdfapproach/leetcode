# https://leetcode.com/problems/calculate-digit-sum-of-a-string/?envType=daily-question&envId=2026-11-16
# Calculate Digit Sum of a String

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k:
            parts = []

            for i in range(0, len(s), k):
                group_sum = sum(int(c) for c in s[i:i + k])
                parts.append(str(group_sum))
            s = "".join(parts)
            
        return s