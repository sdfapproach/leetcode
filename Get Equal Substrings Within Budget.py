# https://leetcode.com/problems/get-equal-substrings-within-budget/?envType=daily-question&envId=2024-05-28
# Get Equal Substrings Within Budget

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
    
        max_length = 0
        current_cost = 0
        left = 0
        
        for right in range(len(s)):
            current_cost += costs[right]
            
            while current_cost > maxCost:
                current_cost -= costs[left]
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length