# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/?envType=daily-question&envId=2026-08-29
# Make Lexicographically Smallest Array by Swapping Elements

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        n = len(nums)

        ordered = sorted((value, i) for i, value in enumerate(nums))
        answer = nums[:]

        start = 0

        while start < n:
            end = start

            while (
                end + 1 < n
                and ordered[end + 1][0] - ordered[end][0] <= limit
            ):
                end += 1

            values = []
            indices = []

            for i in range(start, end + 1):
                value, index = ordered[i]
                values.append(value)
                indices.append(index)

            indices.sort()

            for index, value in zip(indices, values):
                answer[index] = value

            start = end + 1

        return answer