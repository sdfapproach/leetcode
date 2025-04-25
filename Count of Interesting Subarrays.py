# https://leetcode.com/problems/count-of-interesting-subarrays/?envType=daily-question&envId=2025-04-25
# Count of Interesting Subarrays

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        
        prefix_count = defaultdict(int)
        cnt = 0
        result = 0
        prefix_count[0] = 1
        
        for num in nums:
            if num % modulo == k:
                cnt += 1
            
            target = (cnt - k) % modulo
            result += prefix_count[target]
            
            prefix_count[cnt % modulo] += 1
        
        return result