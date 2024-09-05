# https://leetcode.com/problems/find-missing-observations/?envType=daily-question&envId=2024-09-05
# Find Missing Observations

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
        m = len(rolls)
        k = m + n
        
        total_sum = k * mean
        
        observed_sum = sum(rolls)
        
        missing_sum = total_sum - observed_sum
        
        if missing_sum < n or missing_sum > 6 * n:
            return []
        
        quotient, remainder = divmod(missing_sum, n)
        
        result = [quotient] * n
        
        for i in range(remainder):
            result[i] += 1
        
        return result