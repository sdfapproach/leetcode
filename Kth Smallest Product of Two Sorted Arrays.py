# https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/?envType=daily-question&envId=2025-06-25
# Kth Smallest Product of Two Sorted Arrays

from bisect import bisect_right, bisect_left
from typing import List

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:

        def count_no_more_than(x: int) -> int:
            cnt = 0
            for a in nums1:
                if a == 0:
                    if x >= 0:
                        cnt += len(nums2)
                elif a > 0:
                    cnt += bisect_right(nums2, x // a)
                else:  # a < 0
                    q, r = divmod(x, a)
                    if r != 0:
                        q += 1
                    idx = bisect_left(nums2, q)
                    cnt += len(nums2) - idx
            return cnt

        nums1.sort()
        nums2.sort()

        candidates = [
            nums1[0] * nums2[0],
            nums1[0] * nums2[-1],
            nums1[-1] * nums2[0],
            nums1[-1] * nums2[-1],
        ]
        lo, hi = min(candidates), max(candidates)

        answer = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            if count_no_more_than(mid) >= k:
                answer = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return answer