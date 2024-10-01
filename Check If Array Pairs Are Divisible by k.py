# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/?envType=daily-question&envId=2024-10-01
# Check If Array Pairs Are Divisible by k

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        remainder_count = [0] * k
    
        for num in arr:
            remainder = num % k
            remainder_count[remainder] += 1
        
        if remainder_count[0] % 2 != 0:
            return False
        
        for i in range(1, k):
            if remainder_count[i] != remainder_count[k - i]:
                return False
        
        return True