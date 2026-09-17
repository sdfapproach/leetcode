# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/?envType=daily-question&envId=2026-09-17
# Find Two Non-overlapping Sub-arrays Each With Target Sum

class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        
        n = len(arr)

        INF = float('inf')

        best = [INF] * n

        left = 0
        total = 0
        min_len = INF
        answer = INF

        for right in range(n):
            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:
                length = right - left + 1

                if left > 0 and best[left - 1] != INF:
                    answer = min(
                        answer,
                        length + best[left - 1]
                    )

                min_len = min(min_len, length)

            best[right] = min_len

        return -1 if answer == INF else answer