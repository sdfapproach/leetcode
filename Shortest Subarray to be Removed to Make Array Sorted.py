# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/?envType=daily-question&envId=2024-11-15
# Shortest Subarray to be Removed to Make Array Sorted

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        n = len(arr)

        left = 0

        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        if left == n - 1:
            return 0

        right = n - 1

        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        min_remove = min(n - left - 1, right)

        i, j = 0, right

        while i <= left and j < n:
            if arr[i] <= arr[j]:
                min_remove = min(min_remove, j - i - 1)
                i += 1
            else:
                j += 1

        return min_remove