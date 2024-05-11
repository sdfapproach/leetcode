# https://leetcode.com/problems/minimum-cost-to-hire-k-workers/?envType=daily-question&envId=2024-05-11
# Minimum Cost to Hire K Workers

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        
        workers = sorted((w/q, q, w) for q, w in zip(quality, wage))

        res = float('inf')
        qsum = 0
        heap = []

        for ratio, q, w in workers:
            heapq.heappush(heap, -q)
            qsum += q
            
            if len(heap) > k:
                qsum += heapq.heappop(heap)
            
            if len(heap) == k:
                res = min(res, qsum * ratio)
        
        return res