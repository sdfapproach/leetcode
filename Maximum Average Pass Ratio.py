# https://leetcode.com/problems/maximum-average-pass-ratio/?envType=daily-question&envId=2024-12-15
# Maximum Average Pass Ratio

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        pq = []
        for passed, total in classes:
            current_ratio = passed / total
            next_ratio = (passed + 1) / (total + 1)
            heapq.heappush(pq, (-(next_ratio - current_ratio), passed, total))
        
        for _ in range(extraStudents):
            diff, passed, total = heapq.heappop(pq)
            passed += 1
            total += 1
            current_ratio = passed / total
            next_ratio = (passed + 1) / (total + 1)
            heapq.heappush(pq, (-(next_ratio - current_ratio), passed, total))
        
        total_ratio = 0
        while pq:
            _, passed, total = heapq.heappop(pq)
            total_ratio += passed / total
        
        return total_ratio / len(classes)