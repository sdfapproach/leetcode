# https://leetcode.com/problems/count-the-number-of-good-subarrays/?envType=daily-question&envId=2025-04-16
# Count the Number of Good Subarrays

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        if k == 0:
            return n * (n + 1) // 2
        
        ans = 0
        left = 0
        pairs = 0
        freq = defaultdict(int)
        
        for right in range(n):
            pairs += freq[nums[right]]
            freq[nums[right]] += 1
            
            while pairs >= k and left <= right:
                ans += (n - right)
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1
                
        return ans