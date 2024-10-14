# https://leetcode.com/problems/maximal-score-after-applying-k-operations/?envType=daily-question&envId=2024-10-14
# Maximal Score After Applying K Operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        
        # score = 0
        # nums.sort(reverse=True)

        # for i in range(k):

        #     score += nums[0]
        #     nums[0] = math.ceil(nums[0]/3)
        #     nums.sort(reverse=True)

        # return score

        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)

        score = 0

        for _ in range(k):
            max_val = -heapq.heappop(max_heap)
            
            score += max_val
            
            new_val = math.ceil(max_val / 3)
            heapq.heappush(max_heap, -new_val)

        return score