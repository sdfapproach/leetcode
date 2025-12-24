# https://leetcode.com/problems/apple-redistribution-into-boxes/?envType=daily-question&envId=2025-12-24
# Apple Redistribution into Boxes

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        
        total_apples = sum(apple)
        
        capacity.sort(reverse=True)
        
        current_capacity = 0
        count = 0
        
        for cap in capacity:
            current_capacity += cap
            count += 1
            if current_capacity >= total_apples:
                return count
        
        return count