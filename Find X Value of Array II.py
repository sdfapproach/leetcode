# https://leetcode.com/problems/find-x-value-of-array-ii/?envType=daily-question&envId=2026-09-22
# Find X Value of Array II

class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        
        n = len(nums)
        size = 1

        while size < n:
            size *= 2

        prod = [1 % k] * (2 * size)

        cnt = [[0] * k for _ in range(2 * size)]

        for i in range(n):
            value = nums[i] % k
            prod[size + i] = value
            cnt[size + i][value] = 1

        def pull(node):
            left = node * 2
            right = left + 1

            prod[node] = (prod[left] * prod[right]) % k

            new_cnt = cnt[left].copy()

            for r in range(k):
                if cnt[right][r]:
                    nr = (prod[left] * r) % k
                    new_cnt[nr] += cnt[right][r]

            cnt[node] = new_cnt

        for node in range(size - 1, 0, -1):
            pull(node)

        def update(index, value):
            node = size + index
            value %= k

            prod[node] = value
            cnt[node] = [0] * k
            cnt[node][value] = 1

            node //= 2

            while node:
                pull(node)
                node //= 2

        def query(start):
            left = start + size
            right = n + size

            left_prod = 1 % k
            left_cnt = [0] * k

            right_prod = 1 % k
            right_cnt = [0] * k

            def merge(p1, c1, p2, c2):
                new_cnt = c1.copy()

                for r in range(k):
                    if c2[r]:
                        nr = (p1 * r) % k
                        new_cnt[nr] += c2[r]

                return (p1 * p2) % k, new_cnt

            while left < right:
                if left % 2:
                    left_prod, left_cnt = merge(
                        left_prod, left_cnt,
                        prod[left], cnt[left]
                    )
                    left += 1

                if right % 2:
                    right -= 1
                    right_prod, right_cnt = merge(
                        prod[right], cnt[right],
                        right_prod, right_cnt
                    )

                left //= 2
                right //= 2

            return merge(
                left_prod, left_cnt,
                right_prod, right_cnt
            )

        answer = []

        for index, value, start, x in queries:
            update(index, value)

            _, counts = query(start)

            answer.append(counts[x])

        return answer