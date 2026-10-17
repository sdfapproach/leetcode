# https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/?envType=daily-question&envId=2026-10-17
# Minimum Swaps to Sort by Digit Sum

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        def digit_sum(num):
            return sum(int(d) for d in str(num))

        sorted_nums = sorted(
            nums,
            key=lambda x: (digit_sum(x), x)
        )

        position = {
            num: i for i, num in enumerate(sorted_nums)
        }

        visited = [False] * len(nums)
        answer = 0

        for i in range(len(nums)):
            if visited[i]:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = position[nums[j]]
                cycle_size += 1

            if cycle_size > 1:
                answer += cycle_size - 1

        return answer