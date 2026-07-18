# https://leetcode.com/problems/sorted-gcd-pair-queries/?envType=daily-question&envId=2026-07-17
# Sorted GCD Pair Queries

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        
        max_value = max(nums)

        freq = [0] * (max_value + 1)

        for x in nums:
            freq[x] += 1

        exact = [0] * (max_value + 1)

        for d in range(max_value, 0, -1):
            divisible_count = 0

            for multiple in range(d, max_value + 1, d):
                divisible_count += freq[multiple]

            pairs = divisible_count * (divisible_count - 1) // 2

            for multiple in range(d * 2, max_value + 1, d):
                pairs -= exact[multiple]

            exact[d] = pairs

        prefix = [0] * (max_value + 1)

        for d in range(1, max_value + 1):
            prefix[d] = prefix[d - 1] + exact[d]

        answer = []

        for query in queries:
            gcd_value = bisect_right(prefix, query)
            answer.append(gcd_value)

        return answer