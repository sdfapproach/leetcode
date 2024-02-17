# https://leetcode.com/problems/furthest-building-you-can-reach/?envType=daily-question&envId=2024-02-17
# Furthest Building You Can Reach

import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        # jumps = []

        # for i, height in enumerate(heights):
        #     if i < len(heights)-1 and heights[i+1] > height:
        #         jumps.append(heights[i+1] - height)

        # key = sum(jumps)/len(jumps)

        # for i, height in enumerate(heights):

        #     if i < len(heights)-1 and heights[i+1] > height:

        #         if bricks <=0 and ladders <=0:
        #             return i
                
        #         gap = heights[i+1] - height

        #         if gap > key:
        #             ladders -= 1
        #         else:
        #             bricks -= gap

        # return len(heights)

        heap = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(heap, diff)
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i

        return len(heights) - 1