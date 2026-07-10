# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii/?envType=daily-question&envId=2026-07-10
# Path Existence Queries in a Graph II

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        
        ordered = sorted((value, i) for i, value in enumerate(nums))

        values = [value for value, _ in ordered]

        position = [0] * n
        for sorted_idx, (_, original_idx) in enumerate(ordered):
            position[original_idx] = sorted_idx

        component = [0] * n

        for i in range(1, n):
            component[i] = component[i - 1]

            if values[i] - values[i - 1] > maxDiff:
                component[i] += 1

        next_pos = [0] * n

        right = 0

        for left in range(n):
            right = max(right, left)

            while (
                right + 1 < n
                and values[right + 1] - values[left] <= maxDiff
            ):
                right += 1

            next_pos[left] = right

        LOG = n.bit_length()

        jump = [[0] * n for _ in range(LOG)]
        jump[0] = next_pos

        for p in range(1, LOG):
            for i in range(n):
                jump[p][i] = jump[p - 1][jump[p - 1][i]]

        answer = []

        for u, v in queries:
            left = position[u]
            right = position[v]

            if left > right:
                left, right = right, left

            if left == right:
                answer.append(0)
                continue

            if component[left] != component[right]:
                answer.append(-1)
                continue

            current = left
            distance = 0

            for p in range(LOG - 1, -1, -1):
                nxt = jump[p][current]

                if nxt < right and nxt != current:
                    current = nxt
                    distance += 1 << p

            answer.append(distance + 1)

        return answer