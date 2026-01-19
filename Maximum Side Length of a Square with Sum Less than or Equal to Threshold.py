# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/?envType=daily-question&envId=2026-01-19
# Maximum Side Length of a Square with Sum Less than or Equal to Threshold

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        m, n = len(mat), len(mat[0])

        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        def can(k: int) -> bool:
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    total = (
                        prefix[i + k][j + k]
                        - prefix[i][j + k]
                        - prefix[i + k][j]
                        + prefix[i][j]
                    )
                    if total <= threshold:
                        return True
            return False

        left, right = 1, min(m, n)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans