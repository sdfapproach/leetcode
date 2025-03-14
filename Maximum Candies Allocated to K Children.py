# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/?envType=daily-question&envId=2025-03-14
# Maximum Candies Allocated to K Children

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        if sum(candies) < k:
            return 0
            
        left, right = 1, max(candies)
        
        while left < right:
            mid = (left + right + 1) // 2
            
            children = sum(pile // mid for pile in candies)
            
            if children >= k:
                left = mid
            else:
                right = mid - 1
                
        return left