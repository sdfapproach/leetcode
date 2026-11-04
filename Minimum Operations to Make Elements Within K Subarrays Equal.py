# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/?envType=daily-question&envId=2026-11-04
# Minimum Operations to Make Elements Within K Subarrays Equal

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        
        n = len(nums)

        values = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(values)}
        size = len(values)

        count = [0] * (size + 1)
        sums = [0] * (size + 1)

        def update(value, delta):
            i = rank[value]

            while i <= size:
                count[i] += delta
                sums[i] += value * delta
                i += i & -i

        def prefix(i):
            c = 0
            s = 0

            while i > 0:
                c += count[i]
                s += sums[i]
                i -= i & -i

            return c, s

        def kth(target):
            i = 0
            bit = 1 << (size.bit_length() - 1)

            while bit:
                ni = i + bit

                if ni <= size and count[ni] < target:
                    target -= count[ni]
                    i = ni

                bit >>= 1

            return i + 1

        total = 0

        for v in nums[:x]:
            update(v, 1)
            total += v

        costs = []

        for i in range(n - x + 1):
            mid = kth((x + 1) // 2)
            median = values[mid - 1]

            left_count, left_sum = prefix(mid)

            cost = (
                median * left_count - left_sum
                + total - left_sum
                - median * (x - left_count)
            )

            costs.append(cost)

            if i + x < n:
                update(nums[i], -1)
                update(nums[i + x], 1)

                total += nums[i + x] - nums[i]

        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(j * x, n + 1):
                curr[i] = min(
                    curr[i - 1],
                    prev[i - x] + costs[i - x]
                )

            prev = curr

        return prev[n]