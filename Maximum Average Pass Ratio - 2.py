# https://leetcode.com/problems/maximum-average-pass-ratio/?envType=daily-question&envId=2025-09-01
# Maximum Average Pass Ratio

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t

        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1
            heapq.heappush(heap, (-gain(p, t), p, t))

        total = 0.0

        for _, p, t in heap:
            total += p / t

        return total / len(classes)