# https://leetcode.com/problems/maximum-total-subarray-value-ii/?envType=daily-question&envId=2026-06-10
# Maximum Total Subarray Value II

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        
        n = len(nums)

        log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i // 2] + 1

        K = log[n] + 1

        st_max = [[0] * n for _ in range(K)]
        st_min = [[0] * n for _ in range(K)]

        st_max[0] = nums[:]
        st_min[0] = nums[:]

        for p in range(1, K):
            length = 1 << p
            half = length >> 1

            for i in range(n - length + 1):
                st_max[p][i] = max(st_max[p - 1][i], st_max[p - 1][i + half])
                st_min[p][i] = min(st_min[p - 1][i], st_min[p - 1][i + half])

        def range_value(l, r):
            length = r - l + 1
            p = log[length]

            mx = max(st_max[p][l], st_max[p][r - (1 << p) + 1])
            mn = min(st_min[p][l], st_min[p][r - (1 << p) + 1])

            return mx - mn

        heap = []

        for l in range(n):
            val = range_value(l, n - 1)
            heapq.heappush(heap, (-val, l, n - 1))

        ans = 0

        for _ in range(k):
            val, l, r = heapq.heappop(heap)
            ans += -val

            if r - 1 >= l:
                new_val = range_value(l, r - 1)
                heapq.heappush(heap, (-new_val, l, r - 1))

        return ans