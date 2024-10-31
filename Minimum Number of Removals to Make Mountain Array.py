# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/?envType=daily-question&envId=2024-10-30
# Minimum Number of Removals to Make Mountain Array

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 3:
            return -1

        left_lis = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    left_lis[i] = max(left_lis[i], left_lis[j] + 1)

        right_lds = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    right_lds[i] = max(right_lds[i], right_lds[j] + 1)

        max_mountain_len = 0
        for i in range(1, n - 1):
            if left_lis[i] > 1 and right_lds[i] > 1:
                max_mountain_len = max(max_mountain_len, left_lis[i] + right_lds[i] - 1)

        return n - max_mountain_len if max_mountain_len > 0 else -1