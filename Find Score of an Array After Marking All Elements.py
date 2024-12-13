# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/?envType=daily-question&envId=2024-12-13
# Find Score of an Array After Marking All Elements

class Solution:
    def findScore(self, nums: List[int]) -> int:

        n = len(nums)
        score = 0
        marked = [False] * n
        heap = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(heap)

        while heap:
            min_num, idx = heapq.heappop(heap)

            if marked[idx]:
                continue

            score += min_num

            marked[idx] = True
            if idx > 0:
                marked[idx - 1] = True
            if idx < n - 1:
                marked[idx + 1] = True

        return score