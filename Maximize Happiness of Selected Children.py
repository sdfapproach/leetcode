# https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09
# Maximize Happiness of Selected Children

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
    
        total_happiness = 0
        for i in range(k):
            decreased_value = happiness[i] - i
            total_happiness += max(0, decreased_value)
        
        return total_happiness