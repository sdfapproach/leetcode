# https://leetcode.com/problems/make-array-elements-equal-to-zero/?envType=daily-question&envId=2025-10-28
# Make Array Elements Equal to Zero

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        def simulate(start, direction):
            arr = nums[:]
            curr = start
            d = 1 if direction == "right" else -1

            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += d
                else:
                    arr[curr] -= 1
                    d = -d
                    curr += d

            return all(x == 0 for x in arr)

        count = 0
        for i in range(n):
            if nums[i] == 0:
                if simulate(i, "left"):
                    count += 1
                if simulate(i, "right"):
                    count += 1

        return count