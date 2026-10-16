# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/?envType=daily-question&envId=2026-10-16
# Subarrays Distinct Element Sum of Squares II

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if right < start or end < left:
                return 0

            if left <= start and end <= right:
                length = end - start + 1
                old_sum = tree[node]

                tree[node] = (old_sum + length) % MOD
                lazy[node] += 1

                return (2 * old_sum + length) % MOD

            mid = (start + end) // 2

            if lazy[node]:
                value = lazy[node]

                tree[node * 2] += value * (mid - start + 1)
                tree[node * 2 + 1] += value * (end - mid)

                lazy[node * 2] += value
                lazy[node * 2 + 1] += value

                tree[node * 2] %= MOD
                tree[node * 2 + 1] %= MOD

                lazy[node] = 0

            result = (
                update(node * 2, start, mid, left, right)
                + update(node * 2 + 1, mid + 1, end, left, right)
            ) % MOD

            tree[node] = (
                tree[node * 2] + tree[node * 2 + 1]
            ) % MOD

            return result

        last = {}
        current = 0
        answer = 0

        for i, num in enumerate(nums):
            prev = last.get(num, -1)

            increase = update(1, 0, n - 1, prev + 1, i)

            current = (current + increase) % MOD

            answer = (answer + current) % MOD

            last[num] = i

        return answer