# https://leetcode.com/problems/ipo/?envType=daily-question&envId=2024-06-15
# IPO

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
    
        projects = list(zip(capital, profits))
        
        projects.sort()
        
        max_heap = []
        current = 0
        
        for _ in range(k):
            while current < n and projects[current][0] <= w:
                heapq.heappush(max_heap, -projects[current][1])
                current += 1
            
            if not max_heap:
                break
            
            w -= heapq.heappop(max_heap)
        
        return w