# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/?envType=daily-question&envId=2024-12-07
# Minimum Limit of Balls in a Bag

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def canDistribute(mid):
            operations = 0
            for num in nums:
                if num > mid:
                    operations += (num - 1) // mid
            return operations <= maxOperations

        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid
            else:
                left = mid + 1

        return left