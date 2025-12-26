# https://leetcode.com/problems/minimum-penalty-for-a-shop/?envType=daily-question&envId=2025-12-26
# Minimum Penalty for a Shop

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
        n = len(customers)
    
        current_penalty = customers.count('Y')
        min_penalty = current_penalty
        best_hour = 0
        
        for i, char in enumerate(customers):
            if char == 'Y':
                current_penalty -= 1
            else:
                current_penalty += 1
                
            if current_penalty < min_penalty:
                min_penalty = current_penalty
                best_hour = i + 1
                
        return best_hour