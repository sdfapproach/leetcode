# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/?envType=daily-question&envId=2026-10-15
# Subarrays Distinct Element Sum of Squares I

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        
        MOD = 10**9 + 7
        n = len(nums)

        tree = [0] * (4 * n)
        square = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if right < start or end < left:
                return

            if left <= start and end <= right:
                length = end - start + 1

                square[node] += 2 * tree[node] + length
                tree[node] += length
                lazy[node] += 1

                return

            push(node, start, end)

            mid = (start + end) // 2

            update(node * 2, start, mid, left, right)
            update(node * 2 + 1, mid + 1, end, left, right)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]
            square[node] = square[node * 2] + square[node * 2 + 1]

        def push(node, start, end):
            if lazy[node] == 0:
                return

            mid = (start + end) // 2
            value = lazy[node]

            for child, length in [
                (node * 2, mid - start + 1),
                (node * 2 + 1, end - mid)
            ]:
                square[child] += (
                    2 * value * tree[child]
                    + value * value * length
                )

                tree[child] += value * length
                lazy[child] += value

            lazy[node] = 0

        last = {}
        answer = 0

        for i, num in enumerate(nums):
            prev = last.get(num, -1)

            update(1, 0, n - 1, prev + 1, i)

            answer = (answer + square[1]) % MOD
            last[num] = i

        return answer