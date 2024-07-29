# https://leetcode.com/problems/count-number-of-teams/?envType=daily-question&envId=2024-07-29
# Count Number of Teams

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n = len(rating)
        if n < 3:
            return 0
        
        count = 0
        
        for j in range(1, n-1):
            left_less = left_greater = right_less = right_greater = 0
            
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                elif rating[i] > rating[j]:
                    left_greater += 1
            
            for k in range(j+1, n):
                if rating[k] < rating[j]:
                    right_less += 1
                elif rating[k] > rating[j]:
                    right_greater += 1
            
            count += left_less * right_greater
            count += left_greater * right_less
        
        return count