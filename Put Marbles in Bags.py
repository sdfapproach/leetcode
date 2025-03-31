# https://leetcode.com/problems/put-marbles-in-bags/?envType=daily-question&envId=2025-03-31
# Put Marbles in Bags

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        n = len(weights)
        if k == 1:
            return 0
        
        diffs = []
        for i in range(n - 1):
            diffs.append(weights[i] + weights[i + 1])
        
        diffs.sort()
        
        min_sum = sum(diffs[:k - 1])
        max_sum = sum(diffs[-(k - 1):])
        
        return max_sum - min_sum