# https://leetcode.com/problems/minimum-operations-to-sort-a-permutation/?envType=daily-question&envId=2026-10-22
# Minimum Operations to Sort a Permutation

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)

        def check(arr):
            k = arr.index(0)

            for i in range(n):
                if arr[(k + i) % n] != i:
                    return -1

            return k

        answer = float('inf')

        k = check(nums)

        if k != -1:
            answer = min(answer, k)

            answer = min(answer, n - k + 2)

        k = check(nums[::-1])

        if k != -1:
            answer = min(
                answer,
                1 + min(k, n - k)
            )

        return -1 if answer == float('inf') else answer