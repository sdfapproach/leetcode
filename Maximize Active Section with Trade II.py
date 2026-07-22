# https://leetcode.com/problems/maximize-active-section-with-trade-ii/?envType=daily-question&envId=2026-07-22
# Maximize Active Section with Trade II

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        
        n = len(s)
        initial_ones = s.count('1')

        zero_starts = []
        zero_ends = []
        zero_lengths = []

        i = 0

        while i < n:
            if s[i] == '1':
                i += 1
                continue

            start = i

            while i < n and s[i] == '0':
                i += 1

            end = i - 1

            zero_starts.append(start)
            zero_ends.append(end)
            zero_lengths.append(end - start + 1)

        zero_count = len(zero_lengths)

        pair_sum = [
            zero_lengths[i] + zero_lengths[i + 1]
            for i in range(zero_count - 1)
        ]

        pair_count = len(pair_sum)

        if pair_count:
            log = [0] * (pair_count + 1)

            for i in range(2, pair_count + 1):
                log[i] = log[i // 2] + 1

            sparse = [pair_sum[:]]
            power = 1

            while (1 << power) <= pair_count:
                length = 1 << power
                half = length >> 1
                previous = sparse[-1]

                current = [
                    max(previous[i], previous[i + half])
                    for i in range(pair_count - length + 1)
                ]

                sparse.append(current)
                power += 1

            def range_max(left, right):
                if left > right:
                    return 0

                length = right - left + 1
                p = log[length]

                return max(
                    sparse[p][left],
                    sparse[p][right - (1 << p) + 1]
                )

        else:
            def range_max(left, right):
                return 0

        answer = []

        for left, right in queries:
            first = bisect_left(zero_ends, left)

            last = bisect_right(zero_starts, right) - 1

            if first >= zero_count or first >= last:
                answer.append(initial_ones)
                continue

            first_length = (
                min(zero_ends[first], right)
                - max(zero_starts[first], left)
                + 1
            )

            last_length = (
                min(zero_ends[last], right)
                - max(zero_starts[last], left)
                + 1
            )

            if last == first + 1:
                max_gain = first_length + last_length

            else:
                max_gain = first_length + zero_lengths[first + 1]

                max_gain = max(
                    max_gain,
                    zero_lengths[last - 1] + last_length
                )

                max_gain = max(
                    max_gain,
                    range_max(first + 1, last - 2)
                )

            answer.append(initial_ones + max_gain)

        return answer