# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/?envType=daily-question&envId=2026-09-12
# Maximum Score of Non-overlapping Intervals

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        
        n = len(intervals)

        arr = [
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        ]

        arr.sort(key=lambda x: x[1])

        ends = [r for l, r, w, idx in arr]

        prev = [0] * n

        for i, (l, r, w, idx) in enumerate(arr):
            # end < l 이어야 함
            prev[i] = bisect_left(ends, l) - 1

        dp = [
            [(0, ()) for _ in range(5)]
            for _ in range(n + 1)
        ]

        def better(a, b):
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            return a if a[1] < b[1] else b

        for i in range(1, n + 1):
            l, r, w, original_idx = arr[i - 1]

            p = prev[i - 1] + 1

            for k in range(1, 5):
                skip = dp[i - 1][k]

                prev_score, prev_indices = dp[p][k - 1]

                new_indices = tuple(
                    sorted(prev_indices + (original_idx,))
                )

                take = (
                    prev_score + w,
                    new_indices
                )

                dp[i][k] = better(skip, take)

        return list(dp[n][4][1])