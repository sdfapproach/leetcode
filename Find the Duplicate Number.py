# https://leetcode.com/problems/find-the-duplicate-number/?envType=daily-question&envId=2024-03-24
# Find the Duplicate Number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums.sort()

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return nums[i]

        tortoise = hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare