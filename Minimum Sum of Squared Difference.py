# https://leetcode.com/problems/minimum-sum-of-squared-difference/?envType=daily-question&envId=2026-10-10
# Minimum Sum of Squared Difference

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        
        diff = [
            abs(a - b)
            for a, b in zip(nums1, nums2)
        ]

        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left = 0
        right = max(diff)

        while left < right:
            mid = (left + right) // 2

            operations = sum(
                max(0, d - mid)
                for d in diff
            )

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        threshold = left

        for i in range(len(diff)):
            if diff[i] > threshold:
                k -= diff[i] - threshold
                diff[i] = threshold

        answer = sum(d * d for d in diff)

        answer -= k * (2 * threshold - 1)

        return answer